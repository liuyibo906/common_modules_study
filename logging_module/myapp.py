# email liuyibo906@163.com
# 时间 2022/11/28 20:54
import logging
import mylib
def main():
    print('{} is {} years old'.format('liuyib','10'))
    #filename 写入到文件中
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(msg)s',filename='./myapp.log',filemode='w')
    logging.info('started')
    mylib.do_something()
    logging.info('ending')
    name='liuyb'
    age='10'
    print(f"{name} is {age} years old ")
if __name__=='__main__':
    main()