import scrapy


class FreelansimSpider(scrapy.Spider):
    name = 'freelansim'
    a = 0

    start_urls = ['https://freelansim.ru/tasks?page=1&q=python']

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

        with open('1.txt', 'a+') as file:
            self.a = self.a + 1
            file.write(f'{self.a} -')
            yield {
                'title': title,
                'price': price,
                'description': description,
                'link': response.url
            }
