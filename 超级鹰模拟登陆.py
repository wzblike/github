#!/usr/bin/env python
# coding:utf-8

from hashlib import md5

import requests
from lxml import etree


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

#创建一个session对象
session = requests.Session()
url ='https://www.chaojiying.com/user/login/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"}
page_text = session.get(url=url,headers=headers)
page_text.encoding = 'gbk'
page_text=page_text.text
#数据解析
tree = etree.HTML(page_text)
code_path = "https://www.chaojiying.com" + tree.xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img/@src')[0]
# print(code_path)
img_data = session.get(url=code_path, headers=headers).content
imgpath = "./code.jpg"
with open(imgpath, "wb") as fp:
    fp.write(img_data)
    print("下载成功")


chaojiying = Chaojiying_Client('894856408', '15920343558', '908905')	#用户中心>>软件ID 生成一个替换 96001
im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//

code_number = chaojiying.PostPic(im, 1902)['pic_str']#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
print(code_number)
url_new = "https://www.chaojiying.com/user/login/"
data = {
"user":"894856408" ,
"pass": "15920343558",
"imgtxt": code_number,
"act": "1"
}
res =session.post(url=url_new,headers=headers,data=data)
print(res.status_code)

url_neww="https://www.chaojiying.com/user/"
ress=res =session.get(url=url_neww,headers=headers).text
with open('chaoji.html','w',encoding='utf-8') as fp:
    fp.write(ress)




