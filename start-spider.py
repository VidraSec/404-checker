from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from devasec_crawler.spiders.devasec_spider import DevasecSpider



process = CrawlerProcess(get_project_settings())
process.crawl(DevasecSpider)
process.start()