
# 📄🕸️ Selenium Web Scraping of [collegpt](https://www.collegpt.com/)

Welcome to the **Selenium Web Scraping and PDF Automation** project! This repository contains a Python script designed to scrape a webpage and automate the download of PDFs without requiring login credentials.

## 🚀 Project Overview

This project achieves the following:

1. **Chrome WebDriver Setup:** Automatically installs and configures ChromeDriver using `ChromeDriverManager`.
2. **Scraping Links:** Extracts links from webpage elements with the class name `"box"`.
3. **Downloading PDFs:** 
   - Visits each extracted link.
   - Locates the `iframe` element with the class name `"rounded-3xl"`.
   - Extracts the `src` attribute to find the file ID.
   - Constructs a download URL and automatically downloads the PDF.
     
![scrap-gif](https://github.com/omchaudhari1107/Scrap-Collegpt/blob/main/scrap.gif)
## 📦 Dependencies

- Selenium
- WebDriver Manager

To install the necessary dependencies, run:

```bash
pip install selenium webdriver-manager
```

## 🔗 Getting Started

Clone this repository to your local machine:

```bash
git clone https://github.com/omchaudhari1107/Scrap-Collegpt.git
```

## 📥 How It Works

1. **ChromeDriver Setup:** The script uses `ChromeDriverManager` to handle ChromeDriver installation directly in the code.
   
2. **Scraping Process:** 
   - Finds elements with the class name `"box"` and extracts their `href` attributes.
   - Navigates to each link to find the `iframe` with the class `"rounded-3xl"`.
   
3. **PDF Download:** 
   - Extracts the `src` attribute from the `iframe`.
   - Parses the file ID from the `src` URL.
   - Constructs the direct download link using the file ID and downloads the PDF.
