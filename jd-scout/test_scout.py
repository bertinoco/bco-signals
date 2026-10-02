#!/usr/bin/env python3
"""Tests for scout.py.

The regression test runs every entry in docs/data/jobs.json through the filter.
If an entry would have been missed, the keyword list is too narrow: widen
keywords.json rather than special-casing the entry.

Run from the repo root:

    python3 -m unittest jd-scout/test_scout.py
"""

import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scout  # noqa: E402


def archived_text(entry_id):
    path = os.path.join(scout.SOURCE_DIR, entry_id + ".md")
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        return fh.read().split("\n---", 1)[-1]


class Regression(unittest.TestCase):
    def test_every_dataset_entry_matches(self):
        kw = scout.load_keywords()
        with open(scout.JOBS) as fh:
            entries = json.load(fh)["entries"]
        missed = []
        for e in entries:
            match, _ = scout.classify(e["title"], archived_text(e["id"]) or "", kw)
            if not match:
                missed.append("{} ({})".format(e["title"], e["id"]))
        self.assertEqual(missed, [], "entries the scout would have missed")


class Classify(unittest.TestCase):
    kw = scout.load_keywords()

    def test_title_match(self):
        self.assertEqual(scout.classify("Senior UX Writer", "", self.kw)[0], "title")

    def test_title_exclude_wins(self):
        self.assertIsNone(scout.classify("Content Marketing Manager", "content design", self.kw)[0])
        self.assertIsNone(scout.classify("Content Designer, Live Ops (Game)", "", self.kw)[0])

    def test_body_match(self):
        self.assertEqual(scout.classify("Product Designer", "You'll own content design.", self.kw)[0], "body")

    def test_body_only_needs_a_design_or_writing_title(self):
        self.assertIsNone(scout.classify("Credit Risk Manager", "see our tone of voice guide", self.kw)[0])
        self.assertEqual(scout.classify("User Guidance Lead", "content design", self.kw)[0], "body")

    def test_engineering_titles_excluded(self):
        for title in ("Staff Engineer - Content Platform", "Senior Backend Data Engineer – Content Intelligence",
                      "Software Engineer, Tokens and Prompt Structures", "Director of Engineering - Content Platform"):
            self.assertIsNone(scout.classify(title, "", self.kw)[0], title)
        self.assertEqual(scout.classify("Staff Content Engineer", "", self.kw)[0], "title")

    def test_language_vendor_gigs_excluded(self):
        for title in ("AI tester with German language", "Hindi Language Transcription Expert",
                      "Norwegian Language Specialist - Freelance AI Trainer Project",
                      "Evaluators for AI training (English language)"):
            self.assertIsNone(scout.classify(title, "", self.kw)[0], title)
        self.assertEqual(scout.classify("Staff Systems Designer, Language", "", self.kw)[0], "title")

    def test_no_match(self):
        self.assertIsNone(scout.classify("Product Designer", "Figma, prototyping", self.kw)[0])


class Feeds(unittest.TestCase):
    def test_greenhouse_double_escaped_html(self):
        raw = {"jobs": [{"id": 123, "title": "Content Designer", "absolute_url": "u",
                         "location": {"name": "Remote"}, "first_published": "2026-09-01T00:00:00Z",
                         "content": "&lt;p&gt;Own &amp;amp; shape&lt;/p&gt;&lt;ul&gt;&lt;li&gt;UX writing&lt;/li&gt;&lt;/ul&gt;"}]}
        job = scout.normalize("greenhouse", "acme", raw)[0]
        self.assertEqual(job["jobId"], "123")
        self.assertEqual(job["postedDate"], "2026-09-01")
        self.assertIn("Own & shape", job["text"])
        self.assertIn("- UX writing", job["text"])

    def test_lever(self):
        raw = [{"id": "0f1e2d3c-1111-2222-3333-444455556666", "text": "UX Writer",
                "hostedUrl": "u", "categories": {"location": "Berlin"}, "createdAt": 1758000000000,
                "descriptionPlain": "Intro", "lists": [{"text": "You will", "content": "<li>Write</li>"}],
                "additionalPlain": "Benefits", "workplaceType": "hybrid",
                "salaryRange": {"currency": "EUR", "min": 70000, "max": 90000, "interval": "per-year-salary"}}]
        job = scout.normalize("lever", "acme", raw)[0]
        self.assertEqual(job["title"], "UX Writer")
        self.assertIn("You will\n- Write", job["text"])
        self.assertEqual(job["comp"], "EUR 70,000–90,000 per-year-salary")

    def test_ashby_skips_unlisted(self):
        raw = {"jobs": [{"id": "a", "title": "Content Designer", "isListed": False},
                        {"id": "b", "title": "Content Designer", "isListed": True, "isRemote": True,
                         "descriptionPlain": "x", "compensation": {"compensationTierSummary": "$1"}}]}
        jobs = scout.normalize("ashby", "acme", raw)
        self.assertEqual([j["jobId"] for j in jobs], ["b"])
        self.assertEqual(jobs[0]["workplace"], "Remote")


class Urls(unittest.TestCase):
    def test_parse_board_url(self):
        cases = {
            "https://jobs.ashbyhq.com/1password/cf6a76f4-f407": {"ats": "ashby", "slug": "1password"},
            "https://job-boards.greenhouse.io/figma/jobs/5512345": {"ats": "greenhouse", "slug": "figma"},
            "https://boards.greenhouse.io/embed/job_app?for=x": None,
            "https://jobs.eu.lever.co/acme/abc": {"ats": "lever-eu", "slug": "acme"},
            "https://example.com/acme": None,
        }
        for url, want in cases.items():
            self.assertEqual(scout.parse_board_url(url), want, url)

    def test_doc_id_is_a_valid_db_segment(self):
        self.assertEqual(scout.doc_id("ashby", "checkout.com", "88b8"), "ashby-checkout.com-88b8")
        self.assertEqual(scout.doc_id("lever", "a b", "x/y"), "lever-a-b-x-y")


class Poll(unittest.TestCase):
    def test_poll_writes_new_and_skips_known_and_archived(self):
        import tempfile
        from types import SimpleNamespace

        feed = {"jobs": [
            {"id": 1, "title": "Content Designer", "absolute_url": "u1", "content": "x"},
            {"id": 2, "title": "UX Writer", "absolute_url": "u2", "content": "x"},
            {"id": 3, "title": "Account Executive", "absolute_url": "u3", "content": "content design"},
            {"id": 4, "title": "Content Engineer", "absolute_url": "u4", "content": "x"},
        ]}
        real = scout.fetch_json
        scout.fetch_json = lambda url: feed
        try:
            with tempfile.TemporaryDirectory() as tmp:
                companies = os.path.join(tmp, "c.json")
                dump = os.path.join(tmp, "dump")
                os.makedirs(os.path.join(dump, "candidates"))
                os.makedirs(os.path.join(dump, "companies"))
                with open(os.path.join(dump, "candidates", "greenhouse-acme-2.json"), "w") as fh:
                    json.dump({"status": "skip"}, fh)
                with open(os.path.join(dump, "companies", "greenhouse-sanna.json"), "w") as fh:
                    json.dump({"ats": "greenhouse", "slug": "sanna", "name": "Sanna"}, fh)
                with open(os.path.join(dump, "companies", "greenhouse-off.json"), "w") as fh:
                    json.dump({"ats": "greenhouse", "slug": "off", "disabled": True}, fh)
                with open(companies, "w") as fh:
                    json.dump([{"ats": "greenhouse", "slug": "acme", "name": "Acme"},
                               {"ats": "greenhouse", "slug": "sanna", "name": "Sanna"},
                               {"ats": "greenhouse", "slug": "off"}], fh)
                out = os.path.join(tmp, "out")
                scout.cmd_poll(SimpleNamespace(companies=[companies], db_dump=dump, out=out))
                with open(os.path.join(out, "summary.json")) as fh:
                    s = json.load(fh)
                new_boards = sorted(os.listdir(os.path.join(out, "companies-new")))
        finally:
            scout.fetch_json = real
        # Sanna's "Content Engineer" is already in jobs.json, so it is dropped as archived.
        self.assertIn("greenhouse-acme-1", s["newIds"])
        self.assertNotIn("greenhouse-acme-2", s["newIds"])
        self.assertIn("greenhouse-acme-2", s["openIds"])
        self.assertNotIn("greenhouse-acme-3", s["openIds"])
        self.assertNotIn("greenhouse-sanna-4", s["openIds"])
        self.assertIn("greenhouse-acme-4", s["newIds"])
        # Only the board missing from the db is written; the disabled one is not polled.
        self.assertEqual(new_boards, ["greenhouse-acme.json"])
        self.assertEqual(s["companiesChecked"], 2)


if __name__ == "__main__":
    unittest.main()
