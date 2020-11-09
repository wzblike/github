# -*- coding: utf-8 -*-
import scrapy
from movieproject.items import MovieprojectItem
from pymongo.mongo_client import MongoClient
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieSpider(CrawlSpider):
    def __init__(self):
        super().__init__(self)
        #访问MongoDB数据库,专门用来
        self.client=MongoClient("localhost",27017)
        self.url_connection = self.client['moviedb']['urls']
    def __del__(self):
        self.client.close()
    name = 'movie'
    # allowed_domains = ['www.ww.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']
    link=LinkExtractor(allow=r'index1.html')
    link1 = LinkExtractor(allow=r'index1-\d+.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link1, callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        li_list = response.xpath('//div[@class="stui-pannel_bd"]/ul/li')
        for li in li_list:
            self.title = li.xpath('./div/a/@title').extract_first()
            url = li.xpath('./div/a/@href').extract_first()
            #/html/body/div[1]/div/div/div/div[2]/ul/li[1]/div/a
            url ='http://www.4567kan.com/'+str(url)
            # print(title, url)
            cursor = self.url_connection.find({'urls':url})
            if cursor.count()==0:
                print("当前url没有访问过")
                self.url_connection.insert_one({'urls':url})
                yield scrapy.Request(url=url, callback=self.parse_detail)
            else:
                print("当前url已经访问过")
            # yield scrapy.Request(url=url,callback=self.parse_detail)

    def parse_detail(self, response):
        # name = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        desc=response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]//text()').extract_first()
        desc=''.join(desc)
        print(f"电影名称{self.title}\n电影简介:{desc}")

        item = MovieprojectItem()
        item['title']=self.title
        item['desc']=desc
        yield item

