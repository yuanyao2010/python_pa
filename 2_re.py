import re

lst = re.findall(r"\d+","我的电话号是:10086,我女朋友的电话是:10010")
print(lst)
print("-------------------")
it = re.finditer(r"\d+","我的电话号是:10086,我女朋友的电话是:10010")
for i in it:
   print(i.group())
print("---------------------")
s = re.search(r"\d+","我的电话号是:10086,我女朋友的电话是:10010")
print(s.group())
print("-----------------------------")
s = re.match(r"\d+","10086,我女朋友的电话是:10010")
print(s.group())
print("------------------------")

obj = re.compile(r"\d+")
ret =  obj.finditer("我的电话号是:10086,我女朋友的电话是:10010")
for i in ret:
   print(i.group())
print("--------------")

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S)
result = obj.finditer(s)
for it in result:
   print(it.group("wahaha"))
   print(it.group("id"))