import scrapy

class GovSbirAwardSpider(scrapy.Spider):
    name = 'gov.sbir.award'

    start_urls = ["https://www.sbir.gov/sbirsearch/award/all?page=0"]

    def __init__(self):
        for page_num in range(1, 3000):
           self.start_urls.append("https://www.sbir.gov/sbirsearch/award/all?page=%d" % page_num)

    def parse(self, response):
        for li in response.css('ol.apachesolr_search-results > li'):
            sub_title = []
            for span in li.css('div.search-result-sub-title > span'):
                sub_title.append(span.css('::text').extract_first())
            extra = []
            for span in li.css('div.search-result-extra > span'):
                extra.append(span.css('::text').extract_first())
            yield {
                'title': li.css('h3 > a::text').extract_first(),
                'sub_title': sub_title,
                'href': 'https://www.sbir.gov' + li.css('h3 > a::attr(href)').extract_first(),
                'body': li.css('div > p::text').extract_first(),
                'extra': extra
            }
