# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LegobricksItem(scrapy.Item):
    setname = scrapy.Field()
    cost = scrapy.Field()
    age = scrapy.Field()
    pass
