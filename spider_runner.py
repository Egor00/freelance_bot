import os

from scrapy.crawler import CrawlerProcess

from scraper.spider import FreelansimSpider

temp_files = ['1.txt', 'jobs.json']

for file in temp_files:
    if os.path.exists(file):
        os.remove(file)

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'jobs.json'
})

process.crawl(FreelansimSpider, request='python')
process.start()


