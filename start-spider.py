from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from fourOfour_crawler.spiders.fourOfour_spider import fourOfourSpider

process = CrawlerProcess(get_project_settings())
process.crawl(fourOfourSpider)
process.start()
