import sqlite3

# Connect to the database
conn = sqlite3.connect("webcrawler.db")
cursor = conn.cursor()

# Example: Select all crawled URLs and their depths
cursor.execute("SELECT url, depth FROM weblink")
results = cursor.fetchall()

print("Crawled URLs and Depths:")
for row in results:
    print(f"URL: {row[0]}, Depth: {row[1]}\n")

# Additional SQL commands for analysis

# 1. Count the Total Number of Crawled URLs
cursor.execute("SELECT COUNT(*) FROM weblink")
total_urls = cursor.fetchone()[0]
print(f"Total number of crawled URLs: {total_urls}\n")

# 2. Find URLs with the Highest Rank
cursor.execute("SELECT url, rank FROM weblink ORDER BY rank DESC LIMIT 10")
top_urls = cursor.fetchall()
print("Top URLs by rank:")
for row in top_urls:
    print(f"URL: {row[0]}, Rank: {row[1]}\n")

# 3. List URLs with the Most Keywords
cursor.execute("SELECT url, keywords FROM weblink ORDER BY LENGTH(keywords) DESC LIMIT 10")
top_keywords_urls = cursor.fetchall()
print("Top URLs by the number of keywords:")
for row in top_keywords_urls:
    print(f"URL: {row[0]}, Keywords: {row[1]}\n")

# 4. Calculate the Average Depth of Crawled URLs
cursor.execute("SELECT AVG(depth) FROM weblink")
average_depth = cursor.fetchone()[0]
print(f"Average depth of crawled URLs: {average_depth:.2f}\n")

# 5. Find Duplicate URLs
cursor.execute("SELECT url, COUNT(*) FROM weblink GROUP BY url HAVING COUNT(*) > 1")
duplicate_urls = cursor.fetchall()
if duplicate_urls:
    print("Duplicate URLs:")
    for row in duplicate_urls:
        print(f"URL: {row[0]}, Count: {row[1]}\n")
else:
    print("No duplicate URLs found.\n")

# 6. List URLs Crawled at a Specific Depth
target_depth = 5  # Change this to the desired depth
cursor.execute("SELECT url FROM weblink WHERE depth = ?", (target_depth,))
depth_urls = cursor.fetchall()
if depth_urls:
    print(f"URLs crawled at depth {target_depth}:")
    for row in depth_urls:
        print(row[0])
else:
    print(f"No URLs found at depth {target_depth}.\n")

# Close the database connection
conn.close()
