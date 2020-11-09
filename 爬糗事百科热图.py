import os
import re

import requests

if not os.path.exists("./piclib"):
    os.mkdir("./piclib")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"}
url = "https://www.qiushibaike.com/imgrank/"

page_text = requests.get(url=url,headers=headers).text
ex='<div class="thumb">.*?<img src="(.*?)" alt'
img_src_list=re.findall(ex,page_text,re.S)
# print(img_src_list)
for src in img_src_list:
    src="http:"+src
    img_data = requests.get(url=src,headers=headers).content
    img_name = src.split("/")[-1]
    imgpath="./piclib/"+img_name
    with open(imgpath,"wb") as fp:
        fp.write(img_data)
        print(img_name,"下载成功")






