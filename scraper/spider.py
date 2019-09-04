import scrapy
from scraper.datetools import convert_date
from scraper.items import Offer


class FreelansimSpider(scrapy.Spider):
    name = 'freelansim'

    def start_requests(self):
        url = 'https://freelansim.ru/tasks?page=1'
        tag = getattr(self, 'request', None)
        if tag is not None:
            url += '&q=' + tag
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for href in response.css('article.task div header div a::attr(href)'):
            yield response.follow(href, self.parse_offer)
        next_page_selector = response.xpath("//*[@class='next_page']")
        if next_page_selector:
            next_page = response.urljoin(next_page_selector.attrib['href'])
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_offer(self, response):
        title = response.xpath("//*[@class='task__title']/descendant::text()").getall()
        title = ''.join(title).replace('\n', ' ').strip()
        price = response.xpath("//*[@class='task__finance']/descendant::text()").getall()
        price = ''.join(price).replace('\n', ' ').strip()
        description = response.xpath("//*[@class='task__description']/text()").getall()
        description = [part.strip() + '\n' for part in description]
        description = ''.join(description)
        date = response.xpath("//*[@class='task__meta']/text()").getall()[0].strip()[:-3]
        date = convert_date(date)

        with open('1.txt', 'a+') as file:
            file.write(str(date))
        # yield Offer(title=title, price=price, description=description, link=response.url, date=date)
        yield {
            'title': title,
            'price': price,
            'description': description,
            'link': response.url
        }
