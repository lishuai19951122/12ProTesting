# time库案例
import time
# 国外的时间格式
print(time.asctime())
# 时间戳
print(time.time())
# 时间戳转成时间元组
print(time.localtime())
# 将当前的时间戳转成带格式的时间
print(time.strftime('%Y-%m-%d %H：%M：%S', time.localtime()))

# 获取2天前的时间
two_days_bf = time.time()-60*60*24*2
print(time.strftime('%Y-%m-%d %H：%M：%S', time.localtime(two_days_bf)))
