import scrapy
from ..items import JobItem
from ..utils.url_builder import build_indeed_url

class IndeedSpider(scrapy.Spider):
    name = "indeed"
    custom_settings = {"DOWNLOAD_DELAY": 0.5}

    def __init__(self, keyword, **kwargs):
        super().__init__(**kwargs)
        self.keyword = keyword

    def start_requests(self):
        url = build_indeed_url(self.keyword)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for card in response.css("div.jobsearch-SerpJobCard"):
            item = JobItem()
            item["name"] = card.css("span.company::text").get(default="").strip()
            item["title"] = card.css("a.jobtitle::text").get(default="").strip()
            exp_text = card.css("span.experience::text").get(default="0")
            # Extract first integer from experience text
            item["experience"] = int(''.join(filter(str.isdigit, exp_text)) or 0)
            item["url"] = response.urljoin(
                card.css("a.jobtitle::attr(href)").get()
            )
            yield item

        # Pagination: follow "Next" link if present
        next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
