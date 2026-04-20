import scrapy

class BaseSpider(scrapy.Spider):
    def __init__(self, keyword, **kwargs):
        super().__init__(**kwargs)
        self.keyword = keyword
