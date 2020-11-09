# 自己写个小工具,具有的功能有
# 1  验证QQ号(10000开始)  验证邮箱   ip地址   网站是否符合相应的命名规则.
# 2   无聊的时候看看糗事百科,看看最好笑的前20张热图或者随机爬取20张图片,还能爬取段子,还可以找出评论最多的20条段子.
# 3 获取实时热点问题或者关键词
# 4 获取天气信息
# 5  没事学个英语,翻译  输入单词返回解释和例句
#可以先弄一个input 选择功能，然后分别应用，与智能答话一样
import json
import os
import re

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"}
while True:
    answer = input("请输入1-5选择要实现的功能，\n1验证QQ号\n2糗事百科\n3今日微博热点\n4天气\n5英语翻译\n6退出")
    if answer=='1':
        qq = input("请输入你的qq号")
        pattern = r"^[1-9]\d{4,10}$"
        res = re.match(pattern, qq, re.I)
        if  res:
            print("qq号验证成功")
        else:
            print("您输入的不是qq号")
        print()
    elif answer=='2':
        if not os.path.exists("./piclib"):
            os.mkdir("./piclib")

        url = "https://www.qiushibaike.com/imgrank/"
        page_text = requests.get(url=url, headers=headers).text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt'
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            src = "http:" + src
            img_data = requests.get(url=src, headers=headers).content
            img_name = src.split("/")[-1]
            imgpath = "./piclib/" + img_name
            with open(imgpath, "wb") as fp:
                fp.write(img_data)
                print(img_name, "下载成功,打开piclib文件夹查看")
        print()
    elif answer=='3':
        url = "https://s.weibo.com/ajax/jsonp/gettopsug?uid=3655689037&ref=PC_topsug&url=https%3A%2F%2Fd.weibo.com%2F231650%3Fcfs%3D920%26Pl_Discover_Pt6Rank__3_filter%3D%26Pl_Discover_Pt6Rank__3_page%3D1%23Pl_Discover_Pt6Rank__3&Mozilla=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F78.0.3904.108%20Safari%2F537.36&_cb=STK_160267986546412"
        page_text = requests.get(url=url, headers=headers).text
        ex = '"note":"(.*?)"'
        word_list = re.findall(ex, page_text, re.I)
        print("今日微博热点")
        for i in word_list:
            print(i)
        print()
    elif answer=='4':
        Address=input("你想知道哪儿的天气？")
        url ="https://api.seniverse.com/v3/weather/now.json?"
        params={
            "key":"SJLDwClc4-9-0eiU7",
            "location":Address,
            "language":"zh-Hans",
            "unit":"c"
        }
        address_get=requests.get(url=url,params=params)
        address_get=str(address_get.json())
        ex="'text': '(.*?)'"
        address_get1=re.findall(ex, address_get, re.I)
        print(address_get1[0])
        print()
    elif answer=='5':
        url = "https://fanyi.baidu.com/sug"
        word = input("你想查找的单词是什么：")
        data = {
            "kw": word
        }
        # 3 发送请求
        resp = requests.post(url=url, data=data, headers=headers)
        # 4获取我们的响应数据 json方法返回单额是OBJ
        dic_obj = resp.json()
        #转换为json格式用dump，多重字典用dumps
        dic_obj=json.dumps(dic_obj,sort_keys=True, ensure_ascii=False)
        ex='{"k": (.*?)"}'
        dic_obj=re.findall(ex,dic_obj)
        #返回值为列表，循环输出即可
        for i in dic_obj:
            print(i)
        print()
    elif answer=='6':
        print("感谢使用")
        break
    else:
        print("输入有误")














