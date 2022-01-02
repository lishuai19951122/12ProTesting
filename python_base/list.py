# list_hogwarts=[1,5,4,6,3]
# list_hogwarts.append(0)
# list_hogwarts.insert(0,9)
# list_hogwarts.remove(1)
# y = list_hogwarts.pop(0)
# list_hogwarts.sort(reverse=True)
# list_hogwarts.reverse()
# print(y)
# print(list_hogwarts)

# 生成平方列表
# list_test1 = []
# for i in range(1, 4):
#     list_test1.append(i ** 2)
# print(list_test1)
#
# list_test2 = [i ** 2 for i in range(1, 4)]
# print(list_test2)
#
# # 存在条件判断
# list_test3 = [i ** 2 for i in range(1, 4) if i > 1]
# print(list_test3)
#
# # 存在嵌套
# list_test4 = [i*j for i in range(1, 4) for j in range(1, 4)]
# print(list_test4)

# 元组的定义
# tuple_a = (3, 4,4, 5)
# print(tuple_a)
# tuple_b = 1,2,3
# print(tuple_b)
#
# 元组不可变 如果嵌套列表的话可变
# a = [3, 4,4, 5]
# tuple_c = (1, 2, a)
# tuple_c[2][1] = 6
# print(tuple_c)

# # 常用方法
# tuple_a = (3, 4, 4, 5)
# # 统计某个元素在数组中的个数
# print(tuple_a.count(4))
# # 计算某个元素首次出现的索引
# print(tuple_a.index(4))

# 集合的定义
# a = set()
# b = {1}
# print(type(a))
# print(type(b))
# print(len(a))
#
# # 排重字符串元素生成集合
# c = "djaljdflajdfadfaldflakj"
# print(set(c))

# # 常用函数
# a = {1, 2, 3}
# b = {1, 4, 5}
# # 求交集
# print(a.intersection(b))
# # 求并集
# print(a.union(b))
# # 求不同
# print(a.difference(b))
# a.add('b')
# print(a)
# # 集合推导式
# print({i for i in "djajfaldkfja"})

# 定义字典2种方法
# 常用函数
# a = {"a": 1, "b": 2}
# print(a.popitem())
# print(a)

# b = dict(a=1, b=2)
# print(a.keys())
# print(a.values())

# 根据提供的元祖或者列表当作key，生成字典
# a = {}
# print(a.fromkeys([1, 2, 3]))
# print(a.fromkeys((1, 2, 3), "a"))

# 字典推导式
print({i: i ** 2 for i in range(1, 3)})
