import requests
import re

text  = ""
f = open("Data/naver", "r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    text = text+ "".join(line.strip())

# print(s)
# print(type(s))

list = re.findall('<div class="tit">(.+?)<div class="info_mall">', text, re.DOTALL)
for line in list:
    url = re.findall('<a href="(.+?)" class="link"', line)
    price = re.findall('<span class="num _price_reload".+?>(.+?)</span>', line)
    if len(price) > 0:
        print( url,price)





# headers = {'pid': 'UpHFjdpl6HZssmXiBBC-439716',
#             'ssc': 'svc.shopping.v3'
#            }
# headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36'}

# url = 'https://search.shopping.naver.com/search/all.nhn?query=아스파라거스&cat_id=&frm=NVSHATC'
# text= requests.get(url, headers=headers).text
# print(text)
#
# list = re.findall('<div class="tit">(.+?)<div class="info_mall">', text, re.DOTALL)
#
# for line in list:
#     url = re.findall('<a href="(.+?)" class="link"', line)
#     title = re.findall('class="link"(.+?)<span class="price">', line, re.DOTALL)
#     price = re.findall('<span class="num _price_reload".+?>(.+?)</span>', line)
#     print(title, url,price)
#
# list = re.findall('<div class="tit">.+?<a href="(.+?)">.+?<span class="price">', text, re.DOTALL)
# for url in list:
#     print(url)
#




