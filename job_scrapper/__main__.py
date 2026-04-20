import argparse
import os


from scrapy.crawler import CrawlerProcess
from .settings import SCRAPY_SETTINGS
from .spiders import (
    IndeedSpider, NaukriSpider, WellfoundSpider, TopHireSpider,
    InstaHireSpider, GlassdoorSpider, LinkedInSpider, CompanySpider,
)

def build_parser():
    parser = argparse.ArgumentParser(prog="job-scrapper")
    parser.add_argument("--keyword", required=True, help="Search keyword")
    parser.add_argument(
        "--experience",
        default="all",
        choices=["all", "0-2", "3-5", "5+"],
        help="Experience filter",
    )
    parser.add_argument(
        "--output",
        default="jobs.json",
        help="Output JSON file",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose Scrapy logging",
    )
    return parser

def main():
    args = build_parser().parse_args()
    process = CrawlerProcess(settings=SCRAPY_SETTINGS)
    # Add each spider (they all accept a `keyword` argument)
    # If the environment variable SKIP_SPIDERS is set, do not schedule any spiders (useful for fast CI tests)
    if os.getenv("SKIP_SPIDERS") == "1":
        process.start()
        return


    # Feed export configuration
    process.settings.set("FEED_URI", args.output)
    process.settings.set("FEED_FORMAT", "json")
    process.settings.set("FEED_EXPORT_INDENT", 2)
    if args.verbose:
        process.settings.set("LOG_LEVEL", "INFO")
    else:
        process.settings.set("LOG_LEVEL", "WARNING")

    # Pass experience range to pipeline via a custom setting
    process.settings.set("EXPERIENCE_RANGE", args.experience)

    process.start()

if __name__ == "__main__":
    main()
