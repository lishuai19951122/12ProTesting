# # 格式化为带符号的十进制整数
# str = 'my age is %d' % 20
# print(str)
# # 格式化为带符号的十进制整数和字符串
# name = 'lili'
# str1 = 'my name is %s,my age is %d' % (name, 20)
# print(str1)
# # 格式化为带符号的十进制浮点数
# print('pi = %.2f' % 3.1415926)

# * 字符串 举例:
# name = 'Tom'
# name1 = 'Jerry'
# print('two boys are {0} and {1},{0} is tail,{1} is tine'.format(name, name1))
# print('we are the {0} and {1}'.format('Tom', 'Jerry'))
# # * 列表 举例:
# print('we are the {0[0]} and {0[1]}'.format(['Tom', 'Jerry']))
# print('we are the {0} and {1}'.format(*['Tom', 'Jerry']))
# # * 字典 举例:
# # dic = {'name': 'Tom', 'age': '18'}
# print('my name is {name},my age is {age}'.format(**{'name': 'Tom', 'age': '18'}))

# 定义name
name = "JERY"
print(f'my name is {name}')
# 大括号里是函数
print(f'my name is {name.lower()}')
# 大括号里是表达式
print(f'1+1 = {1 + 1}')
