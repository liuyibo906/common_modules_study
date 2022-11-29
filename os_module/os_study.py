# email liuyibo906@163.com
# 时间 2022/11/28 21:15
import os
#1.系统相关
# print(os.name) #系统名称
# print(os.sep) #文件分隔符
# print(os.environ) #环境变量
# print(os.pathsep)  #网址分隔符
# print(os.linesep) #行终止符，win下为"\r\n",Linux下为"\n"
#2.目录操作
# print(os.getcwd())   #获取工作目录
# #os.chdir() #切换工作目录
# print(os.curdir)  #获取当前目录
# print(os.pardir)  #当前目录父目录
# print(os.listdir('./')) #目录下所有目录和文件
#os.remove()  #删除文件
#os.mkdir('dir')  #创建目录
#os.rmdir('dirs')  #删除目录
#os.makedirs('a/b')  #创建多层目录
#os.removedirs('a/b') #删除多曾目录
#print(os.stat('dir'))

# os.path
file=os.getcwd()+os.sep+'os_study.py'
filepath=os.path.join(os.getcwd(),'os_study.py')
# print(os.path.split(file))
# print(os.path.isabs(file)) #是否绝对路径
# #isdir isfile exists
# print(os.path.isdir(file))
# print(os.path.isfile(file))
# print(os.path.exists(file))
#
# #修改时间，创建时间
# print(os.path.getatime(file))  #最近访问时间
# print(os.path.getctime(file)) #创建时间
# print(os.path.getmtime(file)) #修改时间
# print(os.path.getsize(file))

#3.执行命令(现在不推荐使用)，调用系统cmd执行
#os.system('ipconfig')
#os.popen()