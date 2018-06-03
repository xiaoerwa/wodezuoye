# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:08:15 2018

@author: lenovo
"""

weeks=['星期一',
       '星期二',
       '星期三',
       '星期四',
       '星期五',
       '星期六',
       '星期日']
print(weeks[0])
print(weeks[1])
print(weeks[2])
print(weeks[3])
print(weeks[4])
print('今天是:'+weeks[5])
print(weeks[6])


msg={"地址":"北京海淀区xxxx",
 "手机号码":"1838883333",
 "寄信人":'chance'}

print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])


information={"姓名":"赵大帅",
             "身高":"178cm",
             "性别":"男",
             "年龄":"22"}
print(information["姓名"])
print(information["身高"])
print(information["性别"])
print(information["年龄"])



xzhq={'name':'薛之谦',
      'songs':['特别辣','演员','暧昧'],
      '昵称':'xiao薛',
      '认识过女朋友':[2,1,3,8,-1]}
songs=xzhq['songs']
print(songs)
print("歌曲总数:"+str(len(songs)))
print(max(xzhq['认识过女朋友']))


tianqiyubao={"weather":["晴","阴","小雨","大雨","暴雨"],
             "tempture":["37C","39C","36C","33C","30C"],
             "week":["星期一","星期二","星期三","星期四","星期五",]}
print(tianqiyubao["weather"])
xingqi=tianqiyubao["week"]
print("今天是:"+xingqi[3])
print(max(tianqiyubao["tempture"]))



















