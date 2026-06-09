# BCO Content Skills Tracker — Chrome Extension

Submit interesting job postings directly to your content skills tracker repository without scraping or automation.

## What it does

- Click the extension icon on any job posting (LinkedIn, Indeed, company careers pages, etc.)
- Fill in a quick form with job details
- Extension creates a GitHub Issue in your repo with all the metadata
- Reviewer approves, fills in clusters/signals, and merges into `data/jobs.json`

## Setup (5 minutes)

### 1. Create a GitHub Personal Access Token

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Name it: `BCO Skills Tracker Extension`
4. Select scope: **`repo`** (full control of private repositories)
5. Scroll down and click **"Generate token"**
6. **Copy the token immediately** (you won't see it again)

### 2. Load the Extension

1. Open Chrome and go to `chrome://extensions/`
2. Enable **Developer mode** (toggle in top-right)
3. Click **"Load unpacked"**
4. Navigate to this folder (`extension/`) and select it
5. The extension should appear in your toolbar (look for an icon)

### 3. Configure Settings

1. Click the extension icon → click the ⚙️ gear icon
2. Paste your GitHub token into the **"GitHub Personal Access Token"** field
3. Enter your repo: `josephbertino/bco-content-skills-tracker` (or your fork)
4. Click **"Save Settings"**

## Usage

1. Browse to any job posting
2. Click the extension icon in your toolbar
3. The form will auto-fill with:
   - Page URL
   - Job title (if it can be detected)
   - Company (if it can be detected)
4. Fill in required fields:
   - **Company** (if not auto-filled)
   - **Title** (if not auto-filled)
   - **Domain** (e.g., "Fintech", "AI / technology")
5. Optionally fill:
   - Location
   - Posted Date
   - Notes (why this role is interesting, clusters/signals hints, etc.)
6. Click **"Submit"**
7. The extension creates a GitHub Issue in your repo with the candidate job data

## What happens after submission

The extension creates an Issue in `bco-content-skills-tracker` with:

- **Issue title:** `Company — Job Title`
- **Issue body:** structured candidate data with a review checklist
- **Labels:** `candidate-job`, `needs-review`

A reviewer then:
1. Opens the issue
2. Visits the source URL and reviews the full job description
3. Fills in identified clusters and signals
4. Verifies all required fields
5. Closes the issue or creates a PR that merges the entry into `data/jobs.json`

## Troubleshooting

**"GitHub token not set. Visit settings to add your token."**
- Go to extension settings (⚙️ button) and add your token.

**"Failed to create issue"**
- Check that your token has `repo` scope (it allows write access to your repository).
- Check that your repository is in format `owner/repo-name`.
- Verify the token hasn't expired.

**"Issue created! #123" but I don't see it in the repo**
- The issue was created successfully. Check your repo's Issues tab. Make sure you're in the correct repository.

**Page data isn't auto-filled**
- Some job boards use custom HTML that the content script can't parse. Just fill in the fields manually.

## Files

- `manifest.json` — extension configuration
- `popup.html/js` — the main form UI
- `background.js` — GitHub API integration (service worker)
- `content.js` — page data extraction
- `options.html` — settings page for token and repo config

## Development / Debugging

To debug:
1. Go to `chrome://extensions/`
2. Find "BCO Content Skills Tracker" and click "Details"
3. Scroll to "Inspect views" and click `service_worker` to open the background service worker console
4. Or open DevTools on the popup (Inspect) to debug the form

To test locally:
1. Make changes to files
2. Go to `chrome://extensions/` and click the **reload** icon on the extension card
3. Test the extension

## Privacy & Security

- Your GitHub token is stored in Chrome's `chrome.storage.sync` (encrypted by Chrome).
- No data is sent anywhere except to GitHub API.
- The extension only has permissions to read the current page and access GitHub API.
- Raw email/snapshot data is stored in GitHub Issues for audit and provenance.

## Future improvements

- Auto-detect clusters/signals from job description (with human review)
- Export to JSON format (ready to merge into `data/jobs.json`)
- Duplicate detection (warn if similar entry already exists)
- Sync with your personal job alerts (Gmail integration)
