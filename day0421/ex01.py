import requests
import re

f = open('Data/kma.txt', "w",encoding="utf-8")

#도시명, 날짜, 날씨, 최고온도, 최저온도를 파일로 저장해 봅니다.
url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'

text= requests.get(url).text
# print(text)

list = re.findall('<location wl_ver="3">(.+?)</location>',text, re.DOTALL)
#json 형태로 출력해 봅니다.
for location in list:
    city = re.findall('<city>(.+?)</city>', location)[0]
    data_list = re.findall('<data>(.+?)</data>', location, re.DOTALL)
    for data in data_list:
        tmEf = re.findall('<tmEf>(.+?)</tmEf>', data)[0]
        if  tmEf.find("12:00") != -1:
            wf = re.findall('<wf>(.+?)</wf>',data)[0]
            tmx = re.findall('<tmx>(.+?)</tmx>', data)[0]
            tmn = re.findall('<tmn>(.+?)</tmn>', data)[0]
            print(city, tmEf, wf, tmx, tmn)
            f.write(city+"/")
            f.write(tmEf+"/")
            f.write(wf+"/")
            f.write(tmx+"/")
            f.write(tmn+"\n")

f.close()
print('파일로 기록하였습니다.')


# list = re.findall('<province>(.+?)</province>', text)
# print(len(list))
# print(list)

# print(text)
#모든 province 를 출력 해 봅니다.
#city, 날짜, 날씨, 최고온도, 최저온도를 출력 해 봅니다.
