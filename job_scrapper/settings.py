SCRAPY_SETTINGS = {
    "USER_AGENT": "job-scrapper (+https://github.com/yourrepo)",
    "ROBOTSTXT_OBEY": True,
    "DOWNLOAD_DELAY": 0.5,
    "ITEM_PIPELINES": {
        "job_scrapper.pipelines.ExperienceFilter": 300,
    },
}
