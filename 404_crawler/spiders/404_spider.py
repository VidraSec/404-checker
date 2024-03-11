import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class 404Spider(CrawlSpider):
    name = '404_spider'
    # to also see error status codes
    custom_settings = {'handle_httpstatus_all': True}
    # we allow all domains by default, later we only follow links internally
    allowed_domains = []
    # defining the internal domain so we can use localhost
    internal_domain = ["localhost:1337"]
    start_urls = ['http://localhost:1337/']

    rules = (
        # follow links internally
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='a',
                attrs='href',
                unique=True
                ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='link',
                attrs='href',
                unique=True
                ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='script',
                attrs='src',
                unique=True
                ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='img',
                attrs='src',
                unique=True
                ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='iframe',
                attrs='src',
                unique=True
                ),
            follow=True
        ),
        # do not follow links externally (we still check, but we do not follow)
        Rule(
            LinkExtractor(
                tags='a',
                attrs='href',
                unique=True
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='link',
                attrs='href',
                unique=True
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='script',
                attrs='src',
                unique=True
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='img',
                attrs='src',
                unique=True
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='iframe',
                attrs='src',
                unique=True
                ),
            follow=False
        ),
    )
