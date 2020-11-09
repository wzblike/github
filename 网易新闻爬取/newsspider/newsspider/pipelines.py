# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class NewsspiderPipeline(object):
#     def process_item(self, item, spider):
#         print("管道获取的新闻标题和详情内容， 可以实现持久化", item)
#         # 使用文件方式
#         # 使用mysql方式
#         # 使用mongodb方式
#
#         return item
#
# import pymysql
#
#
# # 管道文件中的一个管道类对应 实现一种存储
# class NewsspiderPipeline(object):
#     """
#     1. 导入pymysql模块
#     2. 创建一个Connection连接对象
#     3. 由连接对象 创建游标
#     4. 通过游标执行sql
#     5. 通过游标获取返回的结果
#     6.关闭游标，连接
#     """
#     def __init__(self):
#         print(" 打开数据库连接")
#         # 创建连接对象
#         self.conn = pymysql.Connect(host='127.0.0.1', port=3306,
#                                     database='news', user='root',
#                                     password='1234', charset='utf8')
#         # 通过连接对象创建游标
#         self.cursor = self.conn.cursor()
#
#     def __del__(self):
#         print(" 关闭数据库连接")
#         self.cursor.close()
#         self.conn.close()
#
#     # 专门用来处理item类型对象的
#     # 该方法可以接收爬虫文件 传过来的item对象
#     # 该方法每接收一个item 就会被调用一次
#     def process_item(self, item, spider):
#         title = item['title']
#         content = item['content']
#         try:
#             # 插入操作
#             sql_str = 'insert into news_db(title,content) values("%s","%s")' % (title, content)
#             self.cursor.execute(sql_str)
#             self.conn.commit()  # 提交事务
#         except Exception as e:
#             print(e)
#             self.conn.rollback()  # 回滚事务
#         return item

#
# class NewsspiderPipeline:
#     # fp = None  # 文件对象
#
#     # 编写一个方法， 该方法中只在开始爬虫的时候调用一次
#     def open_spider(self, spider):
#         print("开始爬虫...")
#         self.fp = open("./news.txt", 'w', encoding='utf-8')
#
#     # 专门用来处理item类型对象的
#     # 该方法可以接收爬虫文件 传过来的item对象
#     # 该方法每接收一个item 就会被调用一次
#     def process_item(self, item, spider):
#         title = item['title']
#         content = item['content']
#         self.fp.write(title + ":" + content + "\n")
#         return item
#
#     # 当爬虫结束时调用该方法
#     def close_spider(self, spider):
#         print("爬虫结束...")
#         self.fp.close()
#
#



# -*- coding: utf-8 -*-
from pymongo.mongo_client import MongoClient


class NewsspiderPipeline:
    # 开始爬虫时 回调该方法
    def open_spider(self, spider):
        # 创建mongodb客户端对象
        self.client = MongoClient('localhost', 27017)

        # 创建集合对象
        self.connection = self.client['news']['python']

    def process_item(self, item, spider):
        print("管道获取的新闻标题和详情内容， 可以实现持久化", item)
        # 使用文件方式
        # 使用mysql方式
        # 使用mongodb方式
        self.connection.insert_one({"title": item["title"],
                                    "content": item["content"]})
        return item

    def close_spider(self, spider):
        self.client.close()  # 关闭mongodb的客户端


















