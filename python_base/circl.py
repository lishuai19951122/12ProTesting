# # 计算1-100的和
# result = 0
# for i in range(1,101):
#     result = result +i
# print(result)
#
# # 实现1-100之间的偶数求和
# result =0
# for i in range(2,101,2):
#     result = result +i
# print(result)
# 判断count是否小于5
# count = 1
# while count <5:
#     print(count,'小于5')
#     count = count +1
# else:
#     print(count,'>=5')

# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)
# 实现代码
# import random
# computer_number = random.randint(1,100)
# while True:
#     person_number = int(input('请输入一个正数'))
#     if computer_number > person_number:
#         print('大一点')
#     elif computer_number < person_number:
#         print('小一点')
#     elif computer_number == person_number:
#         print('猜对了')
#         break

# 解包元组
# tupe_a=(3,6)
# print(list(range(*tupe_a)))

# 解包字典
# def method(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# dict ={'a':1,'b':2,'c':3}
# method(**dict)
# lambda 表达式
z = lambda x,y:x+y+7
print(z(1, 2))