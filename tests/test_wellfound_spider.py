import pytest
import scrapy
from job_scrapper.spiders.wellfound import WellfoundSpider
from job_scrapper.items import JobItem
from scrapy.http import TextResponse

def make_response(body: str, url: str = "https://wellfound.com/jobs?q=engineer"):
    return TextResponse(url=url, body=body, encoding='utf-8')

def test_wellfound_spider_parses_item_and_pagination():
    html = """
    <html><body>
        <div class='wf-job-card'>
            <span class='company'>Acme Corp</span>
            <a class='title' href='/job/6789'>Software Engineer</a>
            <span class='exp'>3 years</span>
        </div>
        <a aria-label='Next' href='/jobs?q=engineer&page=2'>Next</a>
    </body></html>
    """
    response = make_response(html)
    spider = WellfoundSpider(keyword='engineer')
    results = list(spider.parse(response))
    assert isinstance(results[0], JobItem)
    item = results[0]
    assert item['name'] == 'Acme Corp'
    assert item['title'] == 'Software Engineer'
    assert item['experience'] == 3
    assert item['url'].endswith('/job/6789')
    # Pagination
    assert isinstance(results[1], scrapy.Request)
    assert results[1].url.endswith('page=2')
