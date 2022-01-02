# 类、方法、类变量的定义
class Person:
    name = 'lili'

    def get_name(self):
        return self.name
# 获取类变量
print(Person.name)
# 获取实例的属性和方法
p = Person()
print(p.name)
print(p.get_name())
# 修改类变量，会影响实力的属性
Person.name = '李帅'
print(Person.name)
print(p.name)
# 修改实例的属性，不会修改类变量
p.name = '李岩'
print(Person.name)
print(p.name)
