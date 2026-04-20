import scrapy

class JobItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    experience = scrapy.Field()  # int, years required
    url = scrapy.Field()
