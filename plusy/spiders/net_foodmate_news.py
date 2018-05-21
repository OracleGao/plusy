import scrapy
import time

class NetFoodmateNewsSpider(scrapy.Spider):
    name = 'news.foodmate.net'

    start_urls = [
        'http://news.foodmate.net/guonei/',
        'http://news.foodmate.net/quanwei/',
        'http://news.foodmate.net/guoji/',
        'http://news.foodmate.net/yujing/',
        'http://news.foodmate.net/keji/',
        'http://news.foodmate.net/daodu/',
        'http://news.foodmate.net/wangyou/',
        'http://news.foodmate.net/qiye/'
    ]

    def parse(self, response):
        for li in response.css('li.catlist_li'):
            dateStr = li.css('span::text').extract_first()
            if dateStr is None:
                continue
            yield {
                'timestamp': dateStr[0:10],
                'href': li.css('a::attr(href)').extract_first(),
                'text': li.css('a::text').extract_first(),
            }
