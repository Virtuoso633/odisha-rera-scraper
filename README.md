# Odisha RERA Project Scraper

This Python script scrapes project details from the Odisha Real Estate Regulatory Authority (RERA) website (`https://rera.odisha.gov.in/projects/project-list`). It extracts information for all projects listed on the initial page, navigates into each project's detail view, and saves the collected data into a CSV file.

## Features

*   Scrapes all projects listed on the main project list page.
*   Navigates into each project's "View" details.
*   Extracts key information from the "Project Overview" and "Promoter Details" tabs.
*   Handles potential click interception issues using JavaScript clicks as a fallback.
*   Saves the scraped data to a CSV file named `odisha_rera_projects.csv`.

## Requirements

*   Python 3.9+
*   The following Python libraries (see `requirements.txt`):
    *   Selenium
    *   Beautiful Soup 4
    *   Pandas
*   Google Chrome browser installed.
*   ChromeDriver:
    *   The script currently expects `chromedriver` to be located at `chromedriver-mac-arm64/chromedriver` relative to the script.
    *   Alternatively, ensure ChromeDriver compatible with your Chrome version is in your system's PATH, or rely on Selenium Manager (included with recent Selenium versions) by removing the explicit `service` object creation in `scraper.py`.

## Setup and Installation

1.  **Clone the repository (if you've already pushed it to GitHub):**
    ```bash
    git clone https://github.com/Virtuoso633/odisha-rera-scraper.git
    cd odisha-rera-scraper
    ```
    If you are setting this up locally first, you can skip this cloning step for now.

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv PrimeNumber_Technologies_venv 
    source PrimeNumber_Technologies_venv/bin/activate
    ```
    (On Windows, use `PrimeNumber_Technologies_venv\Scripts\activate`)

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **ChromeDriver Setup:**
    *   Ensure you have the `chromedriver-mac-arm64/chromedriver` executable in your project directory if you are using the current script's configuration.
    *   Download the correct ChromeDriver version for your Google Chrome browser from [https://developer.chrome.com/docs/chromedriver/downloads](https://developer.chrome.com/docs/chromedriver/downloads).
    *   On macOS, you might need to allow the execution of the downloaded ChromeDriver:
        ```bash
        chmod +x chromedriver-mac-arm64/chromedriver
        xattr -d com.apple.quarantine chromedriver-mac-arm64/chromedriver
        ```

## Usage

Navigate to the project directory in your terminal and run the script:

```bash
python scraper.py
```

The script will print progress messages to the console as it processes each project.

## Output

The script will generate a CSV file named `odisha_rera_projects.csv` in the project directory. The CSV file will contain the following columns:

*   Rera Regd. No
*   Project Name
*   Promoter Name
*   Promoter Address
*   GST No.

## Troubleshooting & Notes

*   **Website Structure Changes**: Web scraping scripts are sensitive to changes in the target website's HTML structure. If the Odisha RERA website is updated, the script might need adjustments to its selectors.
*   **Dynamic Content**: The script uses `WebDriverWait` and `time.sleep()` to handle dynamic content loading. If you encounter issues, these timings or wait conditions might need to be adjusted.
*   **Click Interception**: The script attempts to handle `ElementClickInterceptedException` by falling back to JavaScript clicks.
*   **Network Issues**: Ensure a stable internet connection while running the scraper.
*   **CAPTCHAs**: If the website introduces CAPTCHAs, the script will likely fail and would require manual intervention or a CAPTCHA solving service (which is beyond the scope of this basic scraper).

---
