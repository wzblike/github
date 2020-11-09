# -*- coding: utf-8 -*-
import scrapy
from newsspider.items import NewsspiderItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class NewsSpider(scrapy.Spider):

    name = 'news'
    # allowed_domains = ['www.ss.com']
    start_urls = ['http://news.163.com/']

    def __init__(self):
        super().__init__(self)
        self.module_urls = []
        #实例化一个无头浏览器,且规避检测
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browse=webdriver.Chrome(executable_path=r'C:\second_class\爬虫\day11\newsspider\newsspider\chromedriver.exe',options=chrome_options)

    def parse(self, response):
        li_list = response.xpath('//div[@class="ns_area list"]/ul/li')
        model_indexes = [3,4,6,7,8]
        for index in model_indexes:
            # model_url = li_list[index].xpath('./a/text()').extract_first()
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.module_urls.append(model_url)
        print(self.module_urls)
        for url in self.module_urls:
            yield scrapy.Request(url, callback=self.parse_module, dont_filter=True)
        # yield scrapy.Request("https://news.163.com/domestic/", callback=self.parse_module, dont_filter=True)
        # 解析每一个板块对应的新闻的标题和新闻详情页的url
    def parse_module(self, response):
        # 找不到每一个板块里面的新闻标题 ， 原因是由于前端通过js动态加载的内容
        # print(response.text)
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        print(len(div_list))
        for div in div_list:
            # 新闻标题
            title = div.xpath('.//div[@class="news_title"]/h3/a/text()').extract_first()
            # 某条新闻的详情的url
            content_url = div.xpath('.//div[@class="news_title"]/h3/a/@href').extract_first()

            # 把title的值封装在item中
            item = NewsspiderItem()
            item['title'] = title
            # 当新闻标题不为空，或者新闻详情的url不为空 ，则向某条新闻的新闻详情页面发起请求
            # 把封装了title的item对象 通过meta参数传递给下一个函数(请求的回调函数)
            if title is not None:
                yield scrapy.Request(url=content_url, callback=self.parse_detail, meta={"item": item})

    # 解析 新闻详情页面的函数
    def parse_detail(self, response):
        news_content = response.xpath('//div[@id="content"]//text()').extract()
        news_content = ''.join(news_content)

        # 从上一个函数中传递过来的参数获取新闻标题信息
        item = response.meta['item']
        item['content'] = news_content

        # print(f"url:{response.request.url}, title:{item['title']},  content:{item['content']}")

        # 把item数据持久化
        yield item




    def __del__(self):
        self.browse.quit()