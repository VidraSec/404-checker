import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DevasecSpiderSpider(CrawlSpider):
    name = 'devasec_spider'
    # to also see error status codes
    custom_settings = {'handle_httpstatus_all': True}
    # we allow all domains by default, later we only follow links internally
    allowed_domains = []
    # definding the internal domain so we can use localhost
    # internal_domain = "devasec.org"
    internal_domain = ["localhost:31337"]
    # start_urls = ['https://www.devasec.org/']
    start_urls = ['http://localhost:31337/']

    rules = (
        # follow links internally
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='a',
                attrs='href',
                unique=True
                ),
            callback='parse_item',
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='link',
                attrs='href',
                unique=True
                ),
            callback='parse_item',
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='script',
                attrs='src',
                unique=True
                ),
            callback='parse_item',
            follow=True
        ),
        # do not follow links externally
        Rule(
            LinkExtractor(
                tags='a',
                attrs='href',
                unique=True
                ),
            callback='parse_item',
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='link',
                attrs='href',
                unique=True
                ),
            callback='parse_item',
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='script',
                attrs='src',
                unique=True
                ),
            callback='parse_item',
            follow=False
        ),
    )

    def parse_item(self, response):
        item = {}
        item['url'] = response.url
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
