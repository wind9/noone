# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawl_study.crawl_study.items import BlogArticle
from scrapy import Item


class SinablogSpider(CrawlSpider):
    name = 'sinablog'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/twocold']

    rules = (
        Rule(LinkExtractor(allow=r'twocold$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = BlogArticle(Item)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['title'] = response.xpath('//*[@class="blog_title"]/a/text()')
        item['url'] = response.xpath('//*[@class="blog_title"]/a/@href')
        item['post_time'] = response.xpath('//*[@class="time SG_txtc"]/text()')
        item['comment_count'] = response.xpath('//*[@class="tag SG_txtc"]/text()[1]')
        #tags = response.xpath('')

        return item
