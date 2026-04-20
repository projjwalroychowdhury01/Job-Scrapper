from scrapy.exceptions import DropItem

class ExperienceFilter:
    def __init__(self, experience_range="all"):
        self.range = experience_range

    def process_item(self, item, spider):
        # Pass‑through for now; real filter added later
        return item
