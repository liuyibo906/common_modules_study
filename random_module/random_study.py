# email liuyibo906@163.com
# 时间 2022/11/29 20:52
import  random
#生成随机整数
print(random.randint(1,100))
print(random.randrange(1,101,2))
#random.choice() 随机抽样
list1=list(range(10))
print(list1)
print(random.choice(list1))
#随机抽样多个
print(random.sample(list1,3))
#乱序集合
random.shuffle(list1)
print(list1)
#生成随机浮点数
print(random.random())
print(random.uniform(11.1,11.3))
