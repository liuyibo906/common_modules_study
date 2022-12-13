# email liuyibo906@163.com
# 时间 2022/12/13 21:12
import json
#python对象修改为json string
person={"name":"Sname","age":35,"mobile":['15216772140','15216888521'],"isonly":True}
print(person)
#indent=4,sort_keys=True   格式换输出和排序
jsonstr=json.dumps(person,indent=4,sort_keys=True)
print(jsonstr)
print(type(jsonstr))

json.dump(person,open('data.json','w'),indent=4)

#json string  转换成python对象
pythonObj=json.loads(jsonstr)
print(pythonObj)
print(type(pythonObj))