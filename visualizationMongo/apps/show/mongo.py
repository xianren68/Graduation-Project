# mongodb数据库操作
import pymongo
import random
import pandas as pd
# 创建mongodb连接
def mongoConnect():
    client = pymongo.MongoClient('localhost',27017)
    # 指定数据库
    db = client['Graduation']
    # 指定集合
    collection = db['filmInfo']
    return collection

# 获取所有数据
def getType()->list:
    collection = mongoConnect()
    all_type = [i['types'] for i in collection.find({},{'types':1})]
    return all_type

# 随机获取一部电影
def getRandom()->dict:
    collection = mongoConnect()
    alldocu = []
    for i in collection.find():
        if 'line' in i.keys():
            alldocu.append(i)
    ran = random.randint(0,len(alldocu))
    res =  alldocu[ran]
    res.pop('_id')
    return res

# 获取盈利数据(拥有预算及票房，即mysql,TMDB中的)
def getProfit()->list[dict]:
    collection = mongoConnect()
    profit = []
    for i in collection.find():
        if 'line' in i.keys() and i['budget']!=0 and i['boxoffice']!=0:
            profit.append(i)
    return profit

# 获取评分数据
def getScore()->list[dict]:
    collection = mongoConnect()
    grades = []
    for i in collection.find():
        if 'line' in i.keys():
            grades.append(i)
    return grades

# 获取所有数据
def getAll()->dict:
    collection = mongoConnect()
    data = []
    for i in collection.find({},{'regions':1,'release_date':1}):
        if 'regions' in i:
            i.pop('_id')
            data.append(i)
    data = pd.DataFrame.from_dict(data)
    # 要返回的数据
    res = {}
    # 以年份分组
    data['year'] = pd.to_datetime(data['release_date'],errors = 'coerce').dt.year//10*10
    # 国家数组
    countryArr = data['regions'].tolist()
    # 年份数组
    yearArr = data['year'].tolist()
    res['year'] = yearArr
    res['country'] = countryArr
    return res

# 获取查找的电影
def search(name:str)->dict:
    collection = mongoConnect()
    res = collection.find_one({'title':name})
    res.pop('_id')
    return res