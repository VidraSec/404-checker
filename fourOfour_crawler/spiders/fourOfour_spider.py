import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FourOfourSpider(CrawlSpider):
    name = 'fourOfour_spider'
    # to also see error status codes
    custom_settings = {'handle_httpstatus_all': True}
    # set the download timeout to 5 seconds
    download_timeout = 5
    # we allow all domains by default, later we only follow links internally
    allowed_domains = []
    # defining the internal domain so we can use localhost
    internal_domain = ["localhost:1313"]
    start_urls = ['http://localhost:1313/']

    # ignore LinkedIn and Twitter/X
    # they respond with wrong error codes
    reply_code_wrong = ("linkedin.com", "twitter.com", "x.com")

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
                unique=True,
                deny_extensions=set(), # else defaults to scrapy.linkextractors.IGNORED_EXTENSIONS see: https://stackoverflow.com/a/50165891/492704
                ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='script',
                attrs='src',
                unique=True,
                deny_extensions=set(), # else defaults to scrapy.linkextractors.IGNORED_EXTENSIONS see: https://stackoverflow.com/a/50165891/492704

                ),
            follow=True
        ),
        Rule(
            LinkExtractor(
                allow_domains=internal_domain,
                tags='img',
                attrs='src',
                unique=True,
                deny_extensions=set(), # else defaults to scrapy.linkextractors.IGNORED_EXTENSIONS see: https://stackoverflow.com/a/50165891/492704
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
                unique=True,
                deny_domains=reply_code_wrong,
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='link',
                attrs='href',
                unique=True,
                deny_domains=reply_code_wrong,
                deny_extensions=set(), # else defaults to scrapy.linkextractors.IGNORED_EXTENSIONS see: https://stackoverflow.com/a/50165891/492704
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='script',
                attrs='src',
                unique=True,
                deny_domains=reply_code_wrong,
                deny_extensions=set(), # else defaults to scrapy.linkextractors.IGNORED_EXTENSIONS see: https://stackoverflow.com/a/50165891/492704
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='img',
                attrs='src',
                unique=True,
                deny_domains=reply_code_wrong,
                deny_extensions=set(), # else defaults to scrapy.linkextractors.IGNORED_EXTENSIONS see: https://stackoverflow.com/a/50165891/492704
                ),
            follow=False
        ),
        Rule(
            LinkExtractor(
                tags='iframe',
                attrs='src',
                unique=True,
                deny_domains=reply_code_wrong,
                ),
            follow=False
        ),
    )
