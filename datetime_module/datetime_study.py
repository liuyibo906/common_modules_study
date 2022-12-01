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
t=datetime.time(15,20,31,663999)
print(t,type(t))
#类属性
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)
#实例属性
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
#其他方法
print(t.isoformat())
print(t.strftime('%H:%M:%S'))

print("{:=^50s}".format("datetime.datetime"))

#datetime.datetime
dt=datetime.datetime(2022,2,12,4,2,23,654123)
print(dt,type(dt))

dt=datetime.datetime.today()
print(dt,type(dt))
#时区时间
dt=datetime.datetime.now(tz=None)
print(dt,type(dt))

#时间戳》datetime
dt=datetime.datetime.fromtimestamp(time.time())
print(dt,type(dt))

dt=datetime.datetime.utcfromtimestamp(time.time())
print(dt,type(dt))

#字符串》dt
dt=datetime.datetime.strptime('2022-12-01 13:53:49','%Y-%m-%d %H:%M:%S')
print(dt,type(dt))

dt=datetime.datetime.combine(d,t)
print(dt,type(dt))


#属性
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

#replace
print(dt.replace(year=2020,day=14))


#datetime>结构化时间对象
print(dt.timetuple())

#datetime>时间戳
print(dt.timestamp())
#datetime》格式化字符串
print(dt.strftime('%Y年%m月%d日 %H时%M分%S秒 %f微秒'))


print("{:=^50s}".format("datetime.timedelta"))
#datetime.timedelta
dt=datetime.timedelta(days=10)
print(dt,type(dt))

dt=datetime.timedelta(days=10,hours=15)
print(dt,type(dt))

dt=datetime.datetime.today()
print('现在是{}'.format(dt.strftime('%Y-%m-%d %H:%M:%S')))
delta=datetime.timedelta(days=10)
target=dt+delta
print('现在是{}'.format(target.strftime('%Y-%m-%d %H:%M:%S')))

#计算时间差
dt1=datetime.datetime.today()
dt2=datetime.datetime.utcnow()
dt=dt1-dt2
print(dt.seconds)
print('时间查未：{}小时'.format(dt.seconds/3600))