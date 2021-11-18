import scrapy


class GetWwwSpider(scrapy.Spider):
    name = 'get_www'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        pass
