import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json
import random
import os

# Custom headers to mimic a browser
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
]

# Helper function to get random headers
def get_headers():
    return {"User-Agent": random.choice(USER_AGENTS), "Accept-Language": "en-US,en;q=0.9"}

# Function to scrape Amazon search results
def scrape_amazon(query, pages=20):
    base_url = "https://www.amazon.com/s?k="
    product_list = []

    for page in range(1, pages + 1):
        url = f"{base_url}{query}&page={page}"
        print(f"Scraping URL: {url}")

        try:
            # Add a delay to mimic human browsing
            time.sleep(random.uniform(2, 5))

            # Fetch page content
            response = requests.get(url, headers=get_headers(), timeout=10)

            if response.status_code != 200:
                print(f"Failed to fetch page {page} for query: {query}. HTTP Status: {response.status_code}")
                continue

            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")
            products = soup.select('.s-main-slot .s-result-item')

            for product in products:
                try:
                    title_element = product.select_one('h2 a span')  # Title
                    link_element = product.select_one('h2 a')  # Link
                    reviews_element = product.select_one('.a-size-small .a-link-normal')  # Reviews
                    price_element = product.select_one('.a-price span.a-offscreen')  # Price
                    image_element = product.select_one('.s-image')  # Image URL

                    product_data = {
                        "title": title_element.text.strip() if title_element else "N/A",
                        "link": f"https://www.amazon.com{link_element['href']}" if link_element else "N/A",
                        "reviews": reviews_element.text.strip() if reviews_element else "N/A",
                        "price": price_element.text.strip() if price_element else "N/A",
                        "image_url": image_element['src'] if image_element else "N/A",
                        "creation_timestamp": datetime.now().isoformat(),
                        "scrape_date": datetime.now().date().isoformat(),
                    }

                    # Append to product list if the title or price is valid
                    if product_data["title"] != "N/A" or product_data["price"] != "N/A":
                        product_list.append(product_data)

                except Exception as e:
                    print(f"Error processing product: {e}")
                    continue

        except Exception as e:
            print(f"Error fetching data for query: {query} on page {page}: {e}")
            continue

    return product_list