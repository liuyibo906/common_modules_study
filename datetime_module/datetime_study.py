# email liuyibo906@163.com
# 时间 2022/11/30 21:51
import datetime
import  time
print("{:=^50s}".format("datetime.date"))
d=datetime.date.today()
print(d,type(d))

d=datetime.date(2022,8,23)
print(d,type(d))
#时间戳
d=datetime.date.fromtimestamp(time.time())
print(d,type(d))
#类属性
print(datetime.date.max)
print(datetime.date.min)
print(datetime.date.resolution)
#实例属性
print(d.year)
print(d.month)
print(d.day)

#datetime.date 对象转换未结构化时间对象
print(d.timetuple())

#其他方法 replace
print(d.replace(2020))
print(d.replace(2021,9,12))
print(d.replace(day=10))
print(d.toordinal()) #从0001-01-01 到现在的天数
print(d.weekday()) #0代表周一
print(d.isoweekday()) #1代表周一
print(d.isoformat()) #标准时间格式
print(d.strftime('%Y%m%d'))

print("{:=^50s}".format("datetime.time"))
#生成时间
d=datetime.time(15,20,31,663999)
print(d,type(d))
#类属性
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)
#实例属性
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
#其他方法
print(d.isoformat())
print(d.strftime('%H:%M:%S'))
