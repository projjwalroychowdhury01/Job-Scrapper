import pytest
import scrapy
from scrapy.http import TextResponse
from job_scrapper.spiders.indeed import IndeedSpider
from job_scrapper.items import JobItem

def make_response(body: str, url: str = "https://www.indeed.com/jobs?q=engineer"):
    return TextResponse(url=url, body=body, encoding='utf-8')


def test_indeed_spider_parses_item_and_pagination():
    html = """
    <html><body>
        <div class='jobsearch-SerpJobCard'>
            <span class='company'>Acme Corp</span>
            <a class='jobtitle' href='/rc/clk?jk=12345'>Software Engineer</a>
            <span class='experience'>3 years</span>
        </div>
        <a aria-label='Next' href='/jobs?q=engineer&start=10'>Next</a>
    </body></html>
    """
    response = make_response(html)
    spider = IndeedSpider(keyword='engineer')
    results = list(spider.parse(response))
    # Should yield one JobItem and one Request for next page
    assert isinstance(results[0], JobItem)
    item = results[0]
    assert item['name'] == 'Acme Corp'
    assert item['title'] == 'Software Engineer'
    assert item['experience'] == 3
    assert item['url'].endswith('/rc/clk?jk=12345')
    # Next page request
    assert isinstance(results[1], scrapy.Request)
    assert results[1].url.endswith('start=10')
