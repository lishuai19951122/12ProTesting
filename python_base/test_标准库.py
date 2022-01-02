# 案例
import os
# 创建目录
os.mkdir('testdir')
# 删除目录
os.removedirs('testdir')
# 展示当前目录下的文件
print(os.listdir('../'))
# 获取当面目录路径
print(os.getcwd())
# 判断判断文件 或者目录是否存在
if not os.path.exists('b'):
    os.mkdir('b')
if not os.path.exists('b/test.txt'):
    with open('b/test.txt', 'w') as f:
        f.write('hello,girl')
