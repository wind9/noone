# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from laoyaoba.laoyaoba import LaoyaobaItem
from urllib.parse import urlparse, parse_qs
import requests


class JiweiSpider(CrawlSpider):
    name = 'jiwei'
    allowed_domains = ['laoyaoba.com']
    start_urls = ['https://laoyaoba.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://laoyaoba.com/templates/news/newsdetail.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item = LaoyaobaItem()
        news_url = response.url
        params = urlparse(news_url).query
        item['news_url'] = news_url
        item['news_id'] = parse_qs(params)['news_id'][0]
        item['source'] = parse_qs(params)['source'][0]
        news_html = requests.get(news_url).content
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
