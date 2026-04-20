import scrapy

class BaseSpider(scrapy.Spider):
    def __init__(self, keyword, **kwargs):
        super().__init__(**kwargs)
        self.keyword = keyword

class IndeedSpider(BaseSpider):
    name = "indeed"

class NaukriSpider(BaseSpider):
    name = "naukri"

class WellfoundSpider(BaseSpider):
    name = "wellfound"

class TopHireSpider(BaseSpider):
    name = "tophire"

class InstaHireSpider(BaseSpider):
    name = "instahire"

class GlassdoorSpider(BaseSpider):
    name = "glassdoor"

class LinkedInSpider(BaseSpider):
    name = "linkedin"

class CompanySpider(BaseSpider):
    name = "company"
