a = [1,3,5,7,9,0,2,4,6,8,10,20,30]
# b = a       #얕은 복사  shallow copy
b = a.copy()    #깊은 복사  deep copy
a[0] = 100
print(a)
print(b)


#뒤에서부터 거꾸로 짝수번째만 출력해 봅니다.
# print(a[-2::-2])

# #앞의 반절만 출력해 봅니다.
# print(a[:len(a)//2])
#
# #뒤의 반절만 출력해 봅니다.
# print(a[len(a)//2:])

# print(a[-1:-1])
# print(a[0:1])
# print(a[0:0])

#리스트의 내용을 거꾸로 출력 해 봅니다.
# print(a[len(a)-1:0:-1])
# print(a[len(a)-1:-1:-1])
# print(a[::-1])

# print(a[::2])
# print(a[::])
# print(a[:])
# print(a[:5])
# print(a[3:])
# print(a[0:3])

# print(a[-1])
# print(a[-2])

# print(a[0],a[1])
# print(a[9])
# print(a[len(a)-1])

# print(a)
# print(len(a))