from scrapy.exceptions import DropItem

class ExperienceFilter:
    RANGE_MAP = {
        "all": (None, None),
        "0-2": (0, 2),
        "3-5": (3, 5),
        "5+": (5, None),
    }

    def __init__(self, experience_range="all"):
        self.min, self.max = self.RANGE_MAP.get(experience_range, (None, None))

    @classmethod
    def from_crawler(cls, crawler):
        # Retrieve the custom setting passed from the CLI
        exp_range = crawler.settings.get("EXPERIENCE_RANGE", "all")
        return cls(exp_range)

    def process_item(self, item, spider):
        # Expect "experience" field to be an integer (years)
        exp = int(item.get("experience", 0))
        if self.min is not None and exp < self.min:
            raise DropItem(f"experience {exp} < {self.min}")
        if self.max is not None and exp > self.max:
            raise DropItem(f"experience {exp} > {self.max}")
        return item
