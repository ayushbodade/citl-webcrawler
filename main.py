import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin, urlparse

# Define the seed URL and maximum depth
seed_url = "https://en.wikipedia.org/wiki/Web_crawler"
max_depth = 5

# Initialize the database with the seed link
conn = sqlite3.connect("webcrawler.db")
cursor = conn.cursor()

# Create a table for storing crawled data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weblink (
        id INTEGER PRIMARY KEY,
        url TEXT,
        rank INTEGER,
        keywords TEXT,
        depth INTEGER
    )
''')

# Maintain a set to track visited URLs and avoid duplicates
visited_urls = set()

# Function to extract keywords from the page content (you can implement your own method)
def extract_keywords(soup):
    # This is a placeholder. Implement a method to extract keywords from the page content.
    return "HTTP, webpage, policies"

# Function to crawl a URL and store data in the database
def crawl_url(url, depth, rank, parent_keywords):
    if depth <= max_depth and url not in visited_urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract keywords from the page content (you can use more advanced techniques for this)
                page_keywords = extract_keywords(soup)

                # Insert data into the database
                cursor.execute("INSERT INTO weblink (url, rank, keywords, depth) VALUES (?, ?, ?, ?)",
                               (url, rank, page_keywords, depth))
                conn.commit()

                # Mark the URL as visited to avoid duplicates
                visited_urls.add(url)

                # Crawl links on this page
                links = soup.find_all('a')
                for link in links:
                    next_url = link.get('href')
                    if next_url:
                        # Make the URL absolute by joining it with the base URL
                        next_url = urljoin(url, next_url)

                        # Parse the URL to filter out unwanted links (e.g., external links)
                        parsed_url = urlparse(next_url)
                        if parsed_url.netloc == urlparse(seed_url).netloc:
                            crawl_url(next_url, depth + 1, rank + 1, page_keywords)

        except Exception as e:
            print(f"Error crawling URL {url}: {e}")

# Start the crawl with the seed URL
crawl_url(seed_url, 1, 0, "seed keywords")

# Close the database connection
conn.close()
