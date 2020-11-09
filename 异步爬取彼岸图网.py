import asyncio
import os
import time

import aiohttp
import requests
from lxml import etree

print('一共有171页,建议单次爬取不要超过30页，容易超时')
a=int(input("请输入你的起始页"))
b=int(input("请输入你的结束页"))
start_time=time.time()

if not os.path.exists("./img"):
    os.mkdir("./img")
url = "http://pic.netbian.com/4kmeinv/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"}

async def download_img(url):
    async with aiohttp.ClientSession() as session:
        page_text = requests.get(url=url, headers=headers).text
        #数据解析
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            new_url = 'http://pic.netbian.com/' + li.xpath('./a/@href')[0]
            async with session.get(url=new_url, headers=headers) as response:
                bytes = await response.read()
                page_text_new = bytes.decode(encoding='gbk')
                # 数据解析
                tree1 = etree.HTML(page_text_new)
                img_url = "http://pic.netbian.com" + tree1.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
                img_name = tree1.xpath('//div[@class="photo-pic"]/a/img/@alt')[0]
                # print(img_url)
                # print(img_name)
                img_data = requests.get(url=img_url, headers=headers).content
                imgpath = "./img/" + img_name + '.jpg'
                with open(imgpath, "wb") as fp:
                    fp.write(img_data)
                    print(img_name, "下载成功")

#用于封装协程的任务列表
tasks = []
base_url1 = "http://pic.netbian.com/4kmeinv/index_%d.html"
for page in range(a,b):

    if page >=2:
        base_url = format(base_url1 % page)
    else:
        base_url =url
    c = download_img(base_url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
# 创建一个事件循环对象
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time=time.time()
print(f"共耗时:{end_time-start_time}")