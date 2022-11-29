# email liuyibo906@163.com
# 时间 2022/11/29 21:24
import  time
#的时间戳，从1970年1月1号到当前时间间隔，单位是秒
print(time.time())
print(time.time()-3600)
print(time.ctime())

#结构化时间对象
st=time.localtime()
print(type(st))
print(st)
#st 本质是一个tuple 元组 包含9各元素
print('今天是{}-{:02d}-{}'.format(st[0],st[1],st[2]))
print('今天是星期{}'.format(st.tm_wday+1))

#格式化时间字符串
print(time.ctime())
#strftime(格式)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y年%m月%d日 %H时%M分%S秒'))
print(time.strftime('%Y-%m-%d %H:%M:%S %a'))  #星期 %a
print(time.strftime('%Y-%m-%d %H:%M:%S %A'))  #星期 %A
print(time.strftime('%Y-%m-%d %H:%M:%S %b'))  #月
print(time.strftime('%Y-%m-%d %H:%M:%S %B'))  #月
print(time.strftime('%Y-%m-%d %I:%M:%S %p'))  #12小时制
print(time.strftime('%Y-%m-%d %H:%M:%S %w'))  #本周第二天
print(time.strftime('%Y-%m-%d %H:%M:%S %W'))  #第几周
#等待时间
time.sleep(1.23)

#三种格式的转换
#UTC时间,0时区的时间，格林威治时间,我们时东8区，比它早8小时
#时间戳》结构化对象
print(time.gmtime())
print(time.gmtime(time.time()))

print(time.localtime())
print(time.localtime(time.time()))

#结构化对象》时间戳
print(time.mktime(time.localtime()))
print(time.time())

#结构化对象》格式化字符串
#time.strftime(format,t)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#格式化字符串》结构化对象
#time.strptime()
str='2022-09-20 19:20:10'
print(time.strptime(str,'%Y-%m-%d %H:%M:%S'))


