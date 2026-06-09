// Popup form handler and GitHub API integration

document.addEventListener('DOMContentLoaded', async () => {
  const form = document.getElementById('job-form');
  const submitBtn = document.getElementById('submit-btn');
  const cancelBtn = document.getElementById('cancel-btn');
  const settingsBtn = document.getElementById('settings-btn');
  const statusEl = document.getElementById('status');
  const tokenWarning = document.getElementById('token-warning');

  // Check if token is set
  const { githubToken } = await chrome.storage.sync.get('githubToken');
  if (!githubToken) {
    tokenWarning.style.display = 'block';
  }

  // Get current tab URL and pre-fill
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const sourceUrlInput = document.getElementById('sourceUrl');
  sourceUrlInput.value = tab.url;

  // Extract page data from content script
  try {
    const response = await chrome.tabs.sendMessage(tab.id, { action: 'getPageData' });
    if (response) {
      if (response.title) document.getElementById('title').value = response.title;
      if (response.company) document.getElementById('company').value = response.company;
    }
  } catch (err) {
    // Content script not loaded or page doesn't support it; skip
  }

  // Form submission
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    submitBtn.disabled = true;

    const formData = new FormData(form);
    const data = {
      sourceUrl: formData.get('sourceUrl') || tab.url,
      company: formData.get('company'),
      title: formData.get('title'),
      domain: formData.get('domain'),
      location: formData.get('location'),
      postedDate: formData.get('postedDate'),
      notes: formData.get('notes'),
      alertDate: new Date().toISOString().split('T')[0],
      foundBy: 'extension',
      sourceSnippet: null
    };

    // Validate required fields
    if (!data.company || !data.title || !data.domain) {
      showStatus('error', 'Please fill in all required fields.');
      submitBtn.disabled = false;
      return;
    }

    showStatus('loading', 'Creating GitHub issue...');

    // Send to background script to handle GitHub API call
    try {
      const response = await chrome.runtime.sendMessage({
        action: 'createGitHubIssue',
        data
      });

      if (response.success) {
        showStatus('success', `Issue created! #${response.issueNumber}`);
        setTimeout(() => {
          window.close();
        }, 1500);
      } else {
        showStatus('error', response.error || 'Failed to create issue.');
      }
    } catch (error) {
      showStatus('error', `Error: ${error.message}`);
    }

    submitBtn.disabled = false;
  });

  // Cancel button
  cancelBtn.addEventListener('click', () => {
    window.close();
  });

  // Settings button
  settingsBtn.addEventListener('click', () => {
    chrome.runtime.openOptionsPage();
  });

  function showStatus(type, message) {
    statusEl.className = `status ${type}`;
    statusEl.textContent = message;
  }
});
