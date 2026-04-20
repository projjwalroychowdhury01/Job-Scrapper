from job_scrapper.items import JobItem

def test_item_fields():
    item = JobItem(name="Acme", title="Engineer", experience=3, url="https://example.com")
    assert item["name"] == "Acme"
    assert item["title"] == "Engineer"
    assert item["experience"] == 3
    assert item["url"] == "https://example.com"
