# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlStudyPipeline(object):
    def process_item(self, item, spider):
        for i in range(len(item['titles'])):
            title = item['title'][i]
            url = item['url'][i]
            post_time = item['post_time'][i]
            comment_count = item['comment_count'][i]
            print(title, url, post_time, comment_count)
        return item
