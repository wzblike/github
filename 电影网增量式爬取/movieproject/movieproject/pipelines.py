# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MovieprojectPipeline(object):
    def open_spider(self,spider):
        #取得爬虫对象的MongoDB 客户端对象
        self.client = spider.client
        self.info_collection=self.client['moviedb']['infos']

    def process_item(self, item, spider):
        title = item['title']
        desc = item['desc']
        self.info_collection.insert_one({"title":title,"desc":desc})
        return item
