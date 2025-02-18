# 404 checker

Crawler built on [scrapy](https://github.com/scrapy/scrapy) that helps us find 404 error (or actually any non 200 HTTP status code) on our website.

## start-spider.py

The actual python crawler. It is configured to find all links on our start page, query them all and find new links in the responses, and then query those and so on. This is only done on our domain, for external links, we only query the actual link and do not process the response any further. If we wouldn't have this constraint it could lead to us crawling large parts of the internet.

All HTTP status codes are logged, but we are especially interested in any status code that is not 200 (or redirect) e.g. `404 Not found`. If a non 200 status code is returned, we print it to `stdout`. This is implemented in the middleware.

## start-spider.sh

This is wrapper around the python program. It just starts the python script and exits with an error if any non 200 HTTP codes were returned. This is useful to put the program in a CI pipeline.

## Dependencies

The only real dependency is scrapy. Use their [installation guide](https://docs.scrapy.org/en/latest/intro/install.html).

Example for Ubuntu taken from [Dockerfile](Dockerfile). Of course better use a `venv` if you are on a normal machine (see scrapy install guide):

``` console
# apt-get install -y python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
# pip install -r requirements.txt
```

## How to run

Adapt the settings in [fourOfour_spider.py](fourOfour_crawler/spiders/fourOfour_spider.py):

``` python
internal_domain = ["localhost:1313"]
start_urls = ['http://localhost:1313/']
```

And run

``` console
$ python start-spider.py
```

### Docker

## Example GitHub workflow file

`.github/workflows/hugo-build.yml`

``` yaml
name: Hugo Build and 404 check

on: [push, pull_request]

jobs:
  deploy:
    runs-on: ubuntu-20.04
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - uses: actions/checkout@v3
        with:
          path: website-hugo
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: |
          cd website-hugo
          hugo --minify

      - uses: actions/checkout@v3
        with:
          path: 404-checker
          repository: VidraSec/404-checker

      - name: 404-Check
        run: |
          cd website-hugo
          hugo server &
          cd ..
          sudo apt-get install -y python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
          pip install scrapy
          cd 404-checker
          chmod +x start-spider.sh
          ./start-spider.sh
```

## Misc

[Built by VidraSec](https://www.vidrasec.com)
