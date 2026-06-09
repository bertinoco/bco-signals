// Background service worker — handles GitHub API calls

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'createGitHubIssue') {
    handleCreateIssue(request.data).then(sendResponse);
    return true; // Keep channel open for async response
  }
});

async function handleCreateIssue(data) {
  try {
    const { githubToken, githubRepo } = await chrome.storage.sync.get(['githubToken', 'githubRepo']);

    if (!githubToken) {
      return { success: false, error: 'GitHub token not configured. Visit extension settings.' };
    }

    if (!githubRepo) {
      return { success: false, error: 'GitHub repo not configured. Visit extension settings.' };
    }

    // Parse repo owner/name
    const [owner, repo] = githubRepo.split('/');
    if (!owner || !repo) {
      return { success: false, error: 'Invalid repo format. Use owner/repo-name in settings.' };
    }

    // Build issue body
    const issueBody = buildIssueBody(data);
    const issueTitle = `${data.company} — ${data.title}`;

    // Create GitHub issue
    const response = await fetch(`https://api.github.com/repos/${owner}/${repo}/issues`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${githubToken}`,
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
      },
      body: JSON.stringify({
        title: issueTitle,
        body: issueBody,
        labels: ['candidate-job', 'needs-review']
      })
    });

    if (!response.ok) {
      const error = await response.json();
      return { success: false, error: error.message || 'GitHub API error' };
    }

    const issue = await response.json();
    return { success: true, issueNumber: issue.number, issueUrl: issue.html_url };
  } catch (error) {
    return { success: false, error: error.message };
  }
}

function buildIssueBody(data) {
  return `
**Source URL:** ${data.sourceUrl}

**Company:** ${data.company}  
**Title:** ${data.title}  
**Domain:** ${data.domain}  
**Location:** ${data.location || 'Not specified'}  
**Posted Date:** ${data.postedDate || 'Unknown'}  
**Alert Date:** ${data.alertDate}  

**Curator Notes:**
${data.notes || '(none)'}

---

## Review Checklist
- [ ] JD explicitly supports this role (no inference)
- [ ] Clusters identified and justified
- [ ] Signals identified and justified
- [ ] Company name verified
- [ ] Source URL valid
- [ ] Ready to merge into \`data/jobs.json\`

**Recommended clusters:** (to be filled by reviewer)

**Recommended signals:** (to be filled by reviewer)

**Additional metadata:**
- Found by: ${data.foundBy}
- Data confidence: needs-review

---

To approve this entry:
1. Review the source URL and job description
2. Fill in clusters and signals in the checklist above
3. Add any necessary metadata (compRange, tag, etc.)
4. Check all boxes when complete
5. Close issue or merge the corresponding PR
`;
}
