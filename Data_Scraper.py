# Data Scraper: Extracts news headlines from a website and saves to CSV
import requests
from bs4 import BeautifulSoup
import csv

def scrape_headlines(url, csv_filename):
	try:
		response = requests.get(url)
		response.raise_for_status()
	except requests.RequestException as e:
		print(f"Error fetching the page: {e}")
		return

	soup = BeautifulSoup(response.text, 'html.parser')

	# Example: Extract all <h2> headlines (customize selector as needed)
	headlines = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]

	if not headlines:
		print("No headlines found.")
		return

	try:
		with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(['Headline'])
			for headline in headlines:
				writer.writerow([headline])
		print(f"Saved {len(headlines)} headlines to {csv_filename}")
	except Exception as e:
		print(f"Error writing to CSV: {e}")

if __name__ == "__main__":
	url = input("Enter the URL to scrape: ")
	csv_filename = input("Enter the CSV filename to save results: ")
	scrape_headlines(url, csv_filename)
