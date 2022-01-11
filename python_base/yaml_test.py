# 将yaml格式转换成列表或者字典
import yaml

# 直接转换成列表
print(yaml.load("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
""", Loader=yaml.CLoader))
# 打开文件转换成列表
print(yaml.load(open('test_yaml.txt'), Loader=yaml.CLoader))

with open('dates/test1.yaml', 'w') as f:
    yaml.dump(data=[['Hesperiidae', 'Papilionidae'], ['Apatelodidae', 'Epiplemidae', {'a': 1}]], stream=f)

# 读取一个txt文件，转换成yaml文件
with open('test_yaml.txt', 'rt') as f1:
    while True:
        line = f1.readline()
        if line:
            print(line)
        else:
            break
        with open('dates/test1.yaml', 'w') as f:
            yaml.dump(data=line, stream=f)
