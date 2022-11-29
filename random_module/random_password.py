# email liuyibo906@163.com
# 时间 2022/11/29 21:06
#字符串只包含字符串和数字，指定位数,生成随机密码

import random
import string


def gen_random_string(length):
    numcount=random.randint(1,length-1)
    lettercount=length-numcount
    #print(numcount)
    #string.digits 数字集合，string.ascii_letters 字母集合
    numberlist=[random.choice(string.digits)  for i in range(numcount)]
    letterlist=[random.choice(string.ascii_letters) for i in range(lettercount)]

    alllist=numberlist+letterlist
    random.shuffle(alllist)

    result=''.join(i for i in alllist)
    return  result

for i in range(20):
    password=gen_random_string(64)
    print(password)