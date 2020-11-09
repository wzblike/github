import scrapy
# 导入 QiushibaikeprojectItem 类
from qiushibaikeProject.items import QiushibaikeprojectItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.xyz.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 解析数据 ， 数据失是放在response对象中的
    def parse(self, response):
        # 取作者 以及他发表的content
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # 作者
            # xpath()返回的是列表， 但是列表的元素 一定是 Selector 类型的对象
            # author=div.xpath('./div[1]/a[2]/h2/text()')
            # content=div.xpath('./a[1]/div/span//text()')

            # extract()方法 可以将 Selector对象的data属性的值提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            # 把当前作者的相关数据放在Item中封装起来
            item = QiushibaikeprojectItem()
            # item.author = author
            # item.content = content #该方式赋值会报错
            item['author']=author
            item['content']=content
            # yield工作原理： 挂起当前方法，且该方法处于沉睡状态
            # 把 yield后面的数据作为返回值返回，即返回给管道
            # 当 该方法被唤醒时，则从yield挂起的位置继续往后执行...
            yield item
