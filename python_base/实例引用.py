# 实例引用和实例变量
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def set_att(self, value):
        self.value = value

    def run(self):
        print(f"name is {self.name},gender is {self.gender},age is {self.age},run")

    def eat(self):
        print(f"name is {self.name},gender is {self.gender},age is {self.age},eat")

    def drink(self):
        print(f"name is {self.name},gender is {self.gender},age is {self.age},drink")


p1 = Person('lili', 'male', 18)
print(p1.name)
p1.set_att('fit')
print(p1.value)
p1.run()
