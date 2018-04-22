import scrapy
import time

class HkGovCfsSpider(scrapy.Spider):
    name = 'www.cfs.gov.hk'

    start_urls = ['http://www.cfs.gov.hk/sc_chi/whatsnew/whatsnew_fa/whatsnew_fa.html']

    def parse(self, response):
        for tr in response.css('table.pressTable').xpath('//tr'):
            dateStr = tr.css('td.subHeader::text').extract_first()
            if dateStr is None:
                continue
            date = time.strptime(dateStr, '%d.%m.%Y')
            yield {
                'timestamp': time.strftime("%Y-%m-%d", date),
                'href': 'http://www.cfs.gov.hk' + tr.css('a::attr(href)').extract_first(),
                'text': tr.css('a::text').extract_first(),
            }
