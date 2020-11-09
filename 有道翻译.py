import hashlib
import random
import time

import requests

word=input("请输入你想查找的单词")

def requesturl(data):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data={
        'i':data['i'],
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':data['salt'],
        'sign':data['sign'],
        'lts':data['ts'],
        'bv':data['bv'],
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }
    headers = {
      'Cookie': '_ntes_nnid=c105787715bd01c57557a30e39492d19,1595591833578; OUTFOX_SEARCH_USER_ID_NCOO=561242733.3592136; OUTFOX_SEARCH_USER_ID=-350176089@10.169.0.82; JSESSIONID=aaafF2YPWftcg-p0Vfnwx; ___rl__test__cookies=1604390121889',
      'Origin': 'http://fanyi.youdao.com',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Referer': 'http://fanyi.youdao.com/',
      'X-Requested-With': 'XMLHttpRequest',
      'Connection': 'keep-alive'
    }
    response = requests.request("POST", url, headers=headers, data=data)
    response=response.json()
    print(response)
    print(response['translateResult'][0][0]['tgt'])
    print(response["smartResult"]['entries'])


def getdata(word):
    #时间戳
    ts=str(int(time.time()*1000))
    #标识
    ua="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"
    bv=str(hashlib.md5(ua.encode('utf-8')).hexdigest())
    #盐值
    salt=ts+str(random.randint(1,10))
    #签名
    sign =hashlib.md5(("fanyideskweb"+word+salt+"]BjuETDhU)zqSxf-=B#7m").encode('utf-8')).hexdigest()
    return {"ts":ts,"bv":bv,"salt":salt,"sign":sign,"i":word}

connect = getdata(word)
requesturl(connect)



