import pytest
import scrapy
from job_scrapper.spiders.naukri import NaukriSpider
from job_scrapper.items import JobItem
from scrapy.http import TextResponse

def make_response(body: str, url: str = "https://www.naukri.com/jobs?q=engineer"):
    return TextResponse(url=url, body=body, encoding='utf-8')

def test_naukri_spider_parses_item_and_pagination():
    html = """
    <html><body>
        <div class='job-card'>
            <span class='company'>Acme Corp</span>
            <a class='title' href='/job/12345'>Software Engineer</a>
            <span class='exp'>3 years</span>
        </div>
        <a aria-label='Next' href='/jobs?q=engineer&start=10'>Next</a>
    </body></html>
    """
    response = make_response(html)
    spider = NaukriSpider(keyword='engineer')
    results = list(spider.parse(response))
    assert isinstance(results[0], JobItem)
    item = results[0]
    assert item['name'] == 'Acme Corp'
    assert item['title'] == 'Software Engineer'
    assert item['experience'] == 3
    assert item['url'].endswith('/job/12345')
    # Pagination request
    assert isinstance(results[1], scrapy.Request)
    assert results[1].url.endswith('start=10')
