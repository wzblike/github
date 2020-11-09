import requests
from bs4 import BeautifulSoup

url = "https://www.biduo.cc/biquge/4_4022/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400"}

page_text = requests.get(url=url,headers=headers)
page_text.encoding = 'gbk'
soup = BeautifulSoup(page_text.text,"lxml")
#print(soup)
li_list = soup.select('div #list > dl > dd > a')
# print(li_list)

fp = open("./doupo.txt","w",encoding='utf-8')
for li in li_list:
    title = li.string
    detail_url = 'https://www.biduo.cc/' + li['href']
    # print(detail_url)
    detail_page_text =requests.get(url=detail_url,headers=headers)
    detail_page_text.encoding = 'gbk'
    detail_soup = BeautifulSoup(detail_page_text.text, "lxml")
    # print(detail_soup)
    div_tag = detail_soup.find('div',id="content")
    # print(div_tag.text)
    content = div_tag.text
    fp.write(title+':'+'\n'+content+'\n\n')
    print(title,'爬取成功！！！')
    # print(content)




