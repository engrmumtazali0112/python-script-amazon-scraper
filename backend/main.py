from scraper import scrape_amazon
from utils import read_queries
import pandas as pd
import os
import json

def save_to_csv(all_products, filename="amazon_products.csv"):
    """Save all products to a single CSV file."""
    if not all_products:
        print("No products to save.")
        return
    
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    output_path = os.path.join('output', filename)
    
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(all_products)
    
    # Reorder columns for better readability
    columns_order = [col for col in [
        'title', 'price', 'reviews', 'link', 'image_url', 
        'creation_timestamp', 'scrape_date'
    ] if col in df.columns]
    
    df = df[columns_order]
    
    # Save to CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Saved {len(all_products)} products to {output_path}")

def save_to_json(data, file_path):
    """Save data to a JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving to '{file_path}': {e}")

def main():
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Read queries from the input file
    queries = read_queries('user_queries.json')
    
    if not queries:
        print("No queries found. Exiting...")
        return
    
    all_products = []  # List to store all products from all queries
    
    for query in queries:
        print(f"\nScraping data for query: {query}")
        products = scrape_amazon(query, pages=5)  # Scrape 5 pages per query
        all_products.extend(products)
        save_to_json(products, f'output/{query}.json')  # Save results for each query
        print(f"Found {len(products)} products for query: {query}")
    
    # Save all products to CSV
    save_to_csv(all_products)
    print("\nScraping completed. All data saved to output/amazon_products.csv")

if __name__ == "__main__":
    main()
