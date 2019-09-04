import scrapy


class Offer(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
