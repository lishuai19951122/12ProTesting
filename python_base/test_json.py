import json

# info = [{'name': 'tom',
#          'gender': 'male',
#          'other': None
#          }, {
#             'name': 'Jack',
#             'gender': 'fmale',
#             'other': None
#         }]
#
# # dumps:将pthon中的 字典 转化为 字符串
data = json.dumps(info, sort_keys=True, indent=4)
print(data)
print(type(data))

# dump:将python中的数据类型转换成字符串并存储在文件中
data1 = json.dump(info, open('dates/json_dump.json', 'w'))

# loads:将pthon中字符串转成json
str = '[{"name": "tom", "gender": "male", "other": null}, {"name": "Jack", "gender": "fmale", "other": null}]'
print(json.loads(str))
print(type(json.loads(str)))

# load:把文件打开，把里面的字符转换成json
json_1 = (json.load(open('dates/json_dump.json', 'rt')))
print(json_1)
print(type(json_1))
