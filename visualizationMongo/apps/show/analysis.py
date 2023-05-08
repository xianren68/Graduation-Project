from . import models
import pandas as pd
import pymysql
from . import database
from . import mongo
import functools
import math
import copy
# 获取所有的类型
def getTypes()->dict:
    data =  mongo.getType()
    d = {}
    for i in data:
        l = i.split(',')
        for j in l:
            j = j.strip(" ")
            if j in d.keys():
                d[j]+=1
            else:
                d[j]=1
    return d
# 获取每年上映电影的个数
def getDateNum()->dict:
    data = models.getDateNum()
    # 将年份数据存储到数组中
    for i in data:
        if i[0] == None:
            continue

# 创建数据库连接     
def connect_sql():
        db = pymysql.connect(host="81.70.27.234",port=3306,user="root",
                     password="010825lwj",database="Graduation")
        return db
# 获取所有数据,并将其转换为datafram
def getAll():
    db = connect_sql()
    sql = "select release_date,regions from filmInfo"
    data = pd.read_sql(sql,db)
    db.close()
    return data
# 获取历年排行榜
def getCalenderTop(year:int)->list[dict]:
    data = database.getCalendar(year)
    dL = list(data)
    dL.sort(key=functools.cmp_to_key(compare))
    l = []
    for i in dL:
        d = {}
        d['id'] = i[0]
        d['year'] = i[1]
        d['name'] = i[2]
        d['boxOffice'] = i[3]
        l.append(d)
    return l
# 比较器函数
def compare(x,y)->int:
    if x[3] == y[3]:
        return 0
    elif x[3] > y[3]:
        return -1
    else:
        return 1
# 获取所有类型及其盈利数据
def getTandP(data:list)->dict:
     # dict类型，用于返回
    d = {}
    for i in data:
         profit = i['boxoffice'] - i['budget']
         l = i['types'].split(',')
         for j in l:
            j = j.strip(' ')
            if j in d:
                 d[j].append(profit)
            else:
                d[j] = []
                d[j].append(profit)
    l = d['纪录片']
    d['纪录'] = d['纪录']+l
    d.pop('纪录片')
    # 保存副本
    c = copy.deepcopy(d)
    for i in c:
        if len(d[i])<5:
            d.pop(i)
    return d
# 类型及评分数据
def getTandG(data:list)->dict:
    d = {}
    for i in data:
        grade = i['grade']
        l = i['types'].split(',')
        for j in l:
            j = j.strip(' ')
            if j in d:
                 d[j].append(grade)
            else:
                d[j] = []
                d[j].append(grade)
    l = d['纪录片']
    d['纪录'] = d['纪录']+l
    d.pop('纪录片')
    # 保存副本
    c = copy.deepcopy(d)
    for i in c:
        if len(d[i])<5:
            d.pop(i)
    return d
# 每年国家数量
def countryYear(data:dict):
    res = {}
    for i,j in zip(data['year'],data['country']):
        if math.isnan(i):
            continue
        i = int(i)
        if i not in res:
            res[i] = {}
        for t in j.split(','):
            if t in res[i]:
                res[i][t]+=1
            else:
                res[i][t]=1
    return res