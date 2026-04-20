import pytest
from scrapy.exceptions import DropItem
from job_scrapper.pipelines import ExperienceFilter
from job_scrapper.items import JobItem

def test_filter_all_passes():
    pipe = ExperienceFilter("all")
    item = JobItem(name="X", title="Y", experience=4, url="z")
    assert pipe.process_item(item, None) == item

def test_filter_0_2_allows_in_range():
    pipe = ExperienceFilter("0-2")
    item = JobItem(name="X", title="Y", experience=2, url="z")
    assert pipe.process_item(item, None) == item

def test_filter_0_2_rejects_out_of_range():
    pipe = ExperienceFilter("0-2")
    item = JobItem(name="X", title="Y", experience=5, url="z")
    with pytest.raises(DropItem):
        pipe.process_item(item, None)

def test_filter_5_plus_allows_above():
    pipe = ExperienceFilter("5+")
    item = JobItem(name="X", title="Y", experience=7, url="z")
    assert pipe.process_item(item, None) == item
