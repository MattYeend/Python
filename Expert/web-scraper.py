import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')  # Find all h2 tags
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.text.strip()}")
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

scrape_titles("https://www.bbc.co.uk")
