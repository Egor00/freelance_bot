import scrapy


class FreelansimSpider(scrapy.Spider):
    name = 'freelansim'

    start_urls = ['https://freelansim.ru/tasks?page=1&q=python']

    def parse(self, response):
        for href in response.css('article.task div header div a::attr(href)'):
            yield response.follow(href, self.parse_offer)

    def parse_offer(self, response):
        title = response.xpath("//*[@class='task__title']/descendant::text()").getall()
        title = ''.join(title).replace('\n', ' ').strip()
        price = response.xpath("//*[@class='task__finance']/descendant::text()").getall()
        price = ''.join(price).replace('\n', ' ').strip()
        description = response.xpath("//*[@class='task__description']").getall()
        description = ''.join(description).split('\n')[1:-1]
        description = ''.join(description).replace('<br>', '\n')

        with open('1.txt', 'a+') as file:
            file.write(description)
            yield {
                'title': title,
                'price': price,
                'description': description,
                'link': response.url
            }
