import scrapy
from ..items import JobItem
from ..utils.url_builder import build_naukri_url

class NaukriSpider(scrapy.Spider):
    name = "naukri"
    custom_settings = {"DOWNLOAD_DELAY": 0.5}

    def __init__(self, keyword, **kwargs):
        super().__init__(**kwargs)
        self.keyword = keyword

    def start_requests(self):
        url = build_naukri_url(self.keyword)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for card in response.css("div.job-card"):
            item = JobItem()
            item["name"] = card.css("span.company::text").get(default="").strip()
            item["title"] = card.css("a.title::text").get(default="").strip()
            exp_text = card.css("span.exp::text").get(default="0")
            item["experience"] = int(''.join(filter(str.isdigit, exp_text)) or 0)
            item["url"] = response.urljoin(card.css("a.title::attr(href)").get())
            yield item

        next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
