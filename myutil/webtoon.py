import requests
import re

def getData():
    arr = []
    url = "https://comic.naver.com/webtoon/weekday.nhn"
    text = requests.get(url).text
    list = re.findall('<div class="col_inner">(.+?)</ul>', text, re.DOTALL)
    for line in list:
        li = re.findall("<li>(.+?)</li>", line, re.DOTALL)
        for data in li:
            a = re.findall('src="(.+?)".+? title="(.+?)"', data, re.DOTALL)
            img_url, title = a[0]
            arr.append({"url":img_url, "title":title})
    return arr
