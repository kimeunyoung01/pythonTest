import requests
import  re

url  = 'http://libseat.sogang.ac.kr/seat/roomview5.asp?room_no=6'

data  = requests.get(url).text
text = bytes(data, 'iso-8859-1').decode("euc-kr")

title = re.findall('<FONT SIZE="4"><B>(.+?)</B></FONT>', text);
print(title)

total = re.findall('<b>총 좌석수.+?><b>(.+?)</b></font></td>', text)
print(total)

#연습) 총좌석수를 출력해 봅니다.
