import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1234  Tiger 123
1548  Kerry 534'''

#연습) T로 시작하는 이름만 출력해 봅니다.
startT = re.findall("T[a-z]+",db)
print(startT)

#연습) T로 시작하지 않는 이름만 출력해 봅니다.
# notT = re.findall("[^T][a-z]+",db)
# print(notT)

# notT = re.findall("[ABCDEFGHIJKLMNOPQRSUVXYZ][a-z]+",db)
notT = re.findall("[A-SU-Z][a-z]+",db)
print(notT)





# #연습) id만 출력합니다.
# id_list = re.findall("[0-9]{3}$",db, re.MULTILINE)
# print(id_list)
#
# #연습) 전화번호만 출력합니다.
# tel_list = re.findall("[0-9]{4}", db)
# print(tel_list)





#연습)
#이름만 출력해 봅니다.
# names = re.findall('[A-z]+',db)
# print(names)

#전화번호와 id를 모두 출력해 봅니다.
# r = re.findall('[0-9]+',db)
# print(r)

# print(db)
