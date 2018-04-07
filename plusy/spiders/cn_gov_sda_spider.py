import scrapy

class CnGovSdaSpider(scrapy.Spider):
    name = 'www.sda.gov.cn'

    start_urls = ['http://www.sda.gov.cn/WS01/CL0606/']

    def parse(self, response):
        for td in response.css('td.ListColumnClass15'):
            yield {
                'timestamp': td.css('span.listtddate15::text').extract_first().replace("\r\n", ""),
                'href': td.css('a::attr(href)').extract_first(),
                'text': td.xpath('.//a/font/text()').extract_first(),
            }

