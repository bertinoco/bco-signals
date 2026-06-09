// Content script — extract job data from page

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getPageData') {
    sendResponse(extractJobData());
  }
});

function extractJobData() {
  const data = {
    title: null,
    company: null,
    url: window.location.href
  };

  // Try to extract title from common job board patterns
  // LinkedIn
  const linkedInTitle = document.querySelector('[data-test-job-card-title]')?.textContent ||
                        document.querySelector('.base-main-card h3')?.textContent ||
                        document.querySelector('[aria-label*="job title"]')?.textContent;
  if (linkedInTitle) data.title = linkedInTitle.trim();

  // Indeed
  const indeedTitle = document.querySelector('h1[class*="jobTitle"]')?.textContent ||
                      document.querySelector('.jobsearch-JobInfoHeader-title')?.textContent;
  if (indeedTitle) data.title = indeedTitle.trim();

  // Generic fallback: page title or heading
  if (!data.title) {
    const h1 = document.querySelector('h1');
    if (h1) data.title = h1.textContent.trim().substring(0, 100);
  }

  // Try to extract company
  // LinkedIn
  const linkedInCompany = document.querySelector('[data-test-job-card-subtitle]')?.textContent ||
                          document.querySelector('.base-main-card h4')?.textContent ||
                          document.querySelector('[data-test-topcard-org-name]')?.textContent;
  if (linkedInCompany) data.company = linkedInCompany.trim();

  // Indeed
  const indeedCompany = document.querySelector('[data-company-name]')?.textContent ||
                        document.querySelector('[itemprop="hiringOrganization"]')?.textContent;
  if (indeedCompany) data.company = indeedCompany.trim();

  return data;
}
