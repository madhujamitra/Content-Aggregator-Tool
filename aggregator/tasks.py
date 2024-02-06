from celery import Celery, shared_task
import requests
from bs4 import BeautifulSoup
import os

from aggregator.utils import scrape_aggregations
from aggregator.models import aggregation

# @shared_task
# def scrape_news():
#     sources = [
#         {'url': 'https://example.com/news', 'source': 'Example News'},
#         {'url': 'https://anotherexample.com/news', 'source': 'Another Example News'}
#     ]
#     aggregations = scrape_aggregations(sources)
#     for aggregation in aggregations:
#         aggregation.objects.create(title=aggregation['title'], url=aggregation['url'], source=aggregation['source'])

# @shared_task
# def scrape_url(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     title = soup.title.string
#     new_aggregation = aggregation.objects.create(title=title, url=url, source='Unknown')
#     return new_aggregation

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'content_aggregator.settings')

app = Celery('content_aggregator')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def scrape_url(self, url):
    print('Request: {0!r}'.format(self.request))