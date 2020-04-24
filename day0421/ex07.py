import json

# data = {"name":"이순신", "age":20}
# print(data)
# print(type(data))
#
# r = str(data)
# print(r)
# print(type(r))


data2 = '{"name":"이순신", "age":20}'
print(data2)
print(type(data2))
r = json.loads(data2)
# r = dict(data2)
print(r)
print(type(r))

data3= str(r)
# data3 = json.dumps(r)
print(data3)
print(type(data3))
