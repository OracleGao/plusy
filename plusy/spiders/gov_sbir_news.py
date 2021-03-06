import scrapy

class GovSbirNewsSpider(scrapy.Spider):
    name = 'gov.sbir.news'

    start_urls = ["https://www.sbir.gov/news?page=0"]

    def __init__(self):
        for page_num in range(1, 23):
            self.start_urls.append("https://www.sbir.gov/news?page=%d" % page_num)

    def parse(self, response):
        for div in response.css('div.news-view-rest-wrapper'):
            types = []
            for div_type in div.css('div.news-type > span'):
                types.append(div_type.css('span::text').extract_first())
            yield {
                'title': div.css('div.news-title > a::text').extract_first(),
                'href': 'https://www.sbir.gov' + div.css('div.news-title > a::attr(href)').extract_first(),
                'date': div.css('div.news-date > strong > span::attr(content)').extract_first(),
                'body': div.css('div.news-body::text').extract_first(),
                'type': types
            }
