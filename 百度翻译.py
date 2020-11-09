import requests

#1 指定我们的url

url = "https://fanyi.baidu.com/sug"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"}
#2 post请求参数设置
word = input("word:")
data = {
    "kw":word
}
#3 发送请求
resp = requests.post(url=url,data=data,headers=headers)
#4获取我们的响应数据 json方法返回单额是OBJ
dic_obj = resp.json()
print(dic_obj)
#5储存
#
# filename = word+".json"
# fp = open (filename,"w",encoding="utf-8")
# json.dump(dic_obj,fp=fp,ensure_ascii=False)

print("结束")

