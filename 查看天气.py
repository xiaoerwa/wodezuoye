# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:50:04 2018

#应用其它工具包

@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音:")
print(city_pinyin)
address='http://api.openweathermap.org/data/2.5/weather?q=yibin&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 '
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)



#json转换成(dict)格式工具包
import json
data=json.loads(info)
name=data['name']
t=data['main']['temp']
tm=data['main']['temp_max']
p=data['main']['pressure']

weather=data['weather']
tianqi=weather[0]
tian=tianqi['description']#此段代码等同于  data['weather'][0]['description']



print("欢迎使用全球天气app")
print("1.查看当前城市天气,2.查看其它城市天气,3.保存当前城市")
menno=input("请输入菜单:")

if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
if menno=="3":
    print("3.保存当前城市")

print("当前城市拼音是:"+name)
print("当前温度是:"+str(t))
print("最高温度是:"+str(tm))
print("当前气压是:"+str(p))
print("当前天气是:"+str(tian))






