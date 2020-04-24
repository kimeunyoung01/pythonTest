import requests
import  re


url  = 'https://www.aladin.co.kr/shop/common/wnew.aspx?ViewRowsCount=50&ViewType=Detail&SortOrder=6&page=1&BranchType=1&PublishDay=168&CID=437&NewType=SpecialNew&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption='
data  = requests.get(url).text
# print(data)
#
# list = re.findall('<li><span.+?class="bo3"><b>(.+?)</b></a>.+?<b><span class="">(.+?)</span>원</b></span>', data, re.DOTALL)
list  = re.findall(r'<div class="ss_book_list"><ul>(.+?)</b></li> </ul></div>', data, re.DOTALL)

i = 0
for line in list:
    title = re.findall('class="bo3"><b>(.+?)</b></a>', line)
    price = re.findall('<b><span class="">(.+?)</span>원</b></span>', line)
    date = re.findall('</A>.+?년 (.+?)월</li><li><span class="">', line)
    writer = re.findall( '<li><a href="/Search/.+?>(.+?)</a>', line)
    if int(date[0]) >= 4:
        print(title, price, date, writer)




# list = re.findall('<li><span.+?class="bo3"><b>(.+?)</b></a>.+?</li>', data)
# writer = re.findall('<li><a .+?>(.+?)</a>.+?지은이.+?<A href', data)
# for bookname in list:
#     print(bookname)
# print(len(list))
# print(writer)
# print(len(writer))
