#!/usr/bin/env python3
"""Offline tests for vc_import.py. Run: python3 -m unittest jd-scout/test_vc_import.py"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vc_import  # noqa: E402


class Record(unittest.TestCase):
    def test_board_link(self):
        companies = {}
        vc_import.record(companies, "jt", "Jobandtalent", "https://jobs.lever.co/jobandtalent/4ba29c5d")
        self.assertEqual(companies["jt"]["boards"], {("lever", "jobandtalent")})

    def test_embedded_greenhouse_job_keeps_its_id(self):
        companies = {}
        vc_import.record(companies, "hcp", "Housecall Pro",
                         "https://www.housecallpro.com/careers/open-positions/?gh_jid=6228820004")
        c = companies["hcp"]
        self.assertEqual(c["boards"], set())
        self.assertEqual(c["ghJobIds"], ["6228820004"])
        self.assertEqual(c["otherHosts"], {"www.housecallpro.com": 1})

    def test_other_host_is_counted(self):
        companies = {}
        for _ in range(2):
            vc_import.record(companies, "x", "X", "https://apply.workable.com/x/j/123")
        self.assertEqual(companies["x"]["otherHosts"], {"apply.workable.com": 2})


class Config(unittest.TestCase):
    def test_every_board_has_a_reader(self):
        import json
        with open(os.path.join(vc_import.scout.HERE, "vc-boards.json")) as fh:
            boards = json.load(fh)["boards"]
        for b in boards:
            self.assertIn(b["platform"], vc_import.READERS, b["name"])


if __name__ == "__main__":
    unittest.main()
