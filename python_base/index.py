# 导入方法1
import baidu

print(baidu.a)
print(baidu.add(1, 3))
print(baidu.sub().sub(1, 3))

# 导入方法2
from baidu import a, add, sub

print(a)
print(add(1, 4))
print(sub().sub(1, 4))

# 导入方法3
from baidu import *

print(a)
print(add(1, 4))
print(sub().sub(1, 4))
