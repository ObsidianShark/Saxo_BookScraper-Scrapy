# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BestsellersItem(scrapy.Item):
    # Book description
    price = scrapy.Field()
    member_price = scrapy.Field()
    book_name = scrapy.Field()
    author_name = scrapy.Field()
    book_format = scrapy.Field()
    pages = scrapy.Field()
    publication_date = scrapy.Field()

    # Spider info
    url = scrapy.Field()
    spider = scrapy.Field()
    date = scrapy.Field()
