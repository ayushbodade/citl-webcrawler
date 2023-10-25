**Feature List for the Basic Web Crawler:**

1. **Seed URL:** The crawler begins its journey from a specified seed URL, in this case, "https://en.wikipedia.org/wiki/Web_crawler."

2. **Maximum Depth:** It has a maximum depth limit (`max_depth`) that determines how many levels deep the crawler will traverse from the seed URL.

3. **SQLite Database:** The script initializes and uses an SQLite database to store crawled data, including URL, rank, keywords, and depth.

4. **URL Deduplication:** It maintains a set (`visited_urls`) to prevent crawling the same URL multiple times, ensuring data integrity and efficiency.

5. **Data Extraction:** The script contains a placeholder function (`extract_keywords`) for extracting keywords from the content of web pages. This function can be customized to extract relevant keywords.

6. **Crawling and Link Following:** The crawler sends HTTP GET requests to URLs, parses the HTML content with BeautifulSoup, extracts keywords, and stores the data in the database. It also follows links found on the page to crawl more pages.

7. **URL Normalization:** It ensures that URLs are absolute by joining them with the base URL and filters out unwanted links (e.g., external links).

8. **Error Handling:** The script includes error handling to capture exceptions that may occur during the crawling process and provides informative error messages.

9. **Closing the Database Connection:** It closes the database connection once the crawling process is complete to ensure proper data handling.

10. **Depth Limitation:** The crawler stops when it reaches the specified `max_depth`, preventing it from crawling indefinitely.
