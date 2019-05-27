# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class CrawlStudyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BlogArticle(Item):
    title = Field()
    url = Field()
    post_time = Field()
    read_count = Field()
    comment_count = Field()
    post_count = Field()
    keep_count = Field()
    tags = Field()
