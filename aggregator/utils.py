import requests
from bs4 import BeautifulSoup

def scrape_aggregations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    aggregations = []
    for aggregation in soup.find_all('aggregation'):
        title = aggregation.find('h2').text.strip()
        url = aggregation.find('a')['href']
        author = aggregation.find('span', class_='author').text.strip()
        date = aggregation.find('time')['datetime']
        content = aggregation.find('div', class_='entry-content').text.strip()
        aggregations.append({'title': title, 'url': url, 'author': author, 'date': date, 'content': content})
    for aggregation in aggregations:
        print(f"Title: {aggregation['title']}\nURL: {aggregation['url']}\nAuthor: {aggregation['author']}\nDate: {aggregation['date']}\nContent: {aggregation['content']}\n")
    return aggregations
