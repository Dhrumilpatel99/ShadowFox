# 1. Web Scraper: Extract data from websites using libraries like
# Beautiful Soup or Scrapy.

import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://www.bbc.com/news'

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful or not
if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    # It will find all articles on the page
    articles = soup.find_all('article')


    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        print(f'Title: {title}')
        print(f'Link: {link}')
        print()
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')

headers = {
    'User-Agent': 'Your User-Agent String Here'
}

# Send another request to the URL with the help of headers
response = requests.get(url, headers=headers)

# No further action is taken with the response
