import time
#国际时间
print(time.asctime())
#时间戳
print(time.time())
#时间元组提供格式化
#默认不传值时为当前时间second
print(time.localtime())
print(type(time.localtime()))
#时间格式化
print(time.strftime("%Y %m %d %H:%M:%S", time.localtime()))

#获取两天前时间
now_time=time.time()
two_day_before=now_time - 60*60*24*2
time_tuple=time.localtime(two_day_before)
print(time.strftime("%Y %m %d %H:%M:%S",time_tuple))