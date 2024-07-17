# Zillow Property Scraper

This project is a Zillow property scraper that extracts data from the Zillow clone website and populates a Google Form with the extracted details. The Google Form responses can then be exported to a Google Sheet for easy data analysis.

## Prerequisites

To run this project, you will need:

- Python 3.x
- Selenium
- BeautifulSoup
- Google Chrome browser
- ChromeDriver

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Prathamesh326/Data-Entry-Job-Automation.git
    cd Data-Entry-Job-Automation
    ```

2. **Install Dependencies**

    Install the required Python libraries using pip:

    ```bash
    pip install requests beautifulsoup4 selenium
    ```

3. **Download ChromeDriver**

    Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it matches your Chrome browser version. Place the ChromeDriver executable in a directory included in your system's PATH or in the same directory as your script.

4. **Create a Google Form**

    - Create a Google Form with the following fields:
      - Address (Short answer)
      - Price per Month (Short answer)
      - Property Link (Short answer)
    - Obtain the URL of the form and update the `GOOGLE_FORM` variable in the script.

## Usage

1. **Run the Script**

    ```bash
    python main.py
    ```

    The script will:
    - Scrape property data (addresses, prices, and links) from the Zillow clone website.
    - Populate the Google Form with the scraped data.

2. **Check Google Form Responses**

    - Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form.
    - You should end up with a spreadsheet containing all the details from the properties.
