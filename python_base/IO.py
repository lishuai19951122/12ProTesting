# f = open('dates/test.txt','rt')
# 使用readline方法读取文件
with open('dates/test.txt', 'rt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break

