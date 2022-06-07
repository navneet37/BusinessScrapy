import scrapy


class UaIpTestSpider(scrapy.Spider):
    name = 'ua_ip_test'
    allowed_domains = ['httpbin.org']
    # start_urls = ['http://httpbin.org/ip']
    start_urls = ['https://httpbin.org/user-agent']

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        response_item = response.json()
        yield {"ip": response_item}
