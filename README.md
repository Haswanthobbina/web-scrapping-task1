# Web Scraper for Quotes (Top 100 Quotes)
This Python script is a simple **web scraper** that collects the **top 100 quotes** from the website (https://quotes.toscrape.com) and saves them into a CSV file named `quotes.csv`.

Each quote includes:
- The quote text
- The author name
**requests** – To fetch content from the website (HTML of the page).
**BeautifulSoup (bs4)** – To parse and extract data from the HTML.
The script uses a `while` loop to go through all pages of the website one by one using the "Next" button **csv** – To save the scraped data in CSV format.

