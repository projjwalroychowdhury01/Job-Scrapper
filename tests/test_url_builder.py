from job_scrapper.utils.url_builder import build_indeed_url


def test_build_indeed_url_contains_query():
    url = build_indeed_url("engineer")
    assert "q=engineer" in url
