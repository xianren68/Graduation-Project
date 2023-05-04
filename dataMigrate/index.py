# mysql驱动
import pymysql
# mongodb驱动
import pymongo
# 创建mysql数据库连接
import datetime
def mysqlConnect():
    db = pymysql.connect(host="81.70.27.234", port=3306, user="root",
                         password="010825lwj", database="Graduation")
    return db
# 创建mongodb连接
def mongoConnect():
    client = pymongo.MongoClient('localhost',27017)
    db = client['Graduation']
    return db
# 读取mysql,FilmInfo数据
def getMysqlFilmInfo()->dict:
    sql = 'select * from filmInfo'
    db = mysqlConnect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data
# 读取mysql,TMDB数据
def getMysqlTMDB()->dict:
    sql = 'select * from TMDB'
    db = mysqlConnect()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data
# 向mongodb写入数据
def saveMongo(data:list):
    db = mongoConnect()
    # 选择集合
    collection = db['filmInfo']
    # 插入json数组
    collection.insert_many(data)
# mongodb更新数据
def mongoUpdate(data:dict):
    # 删除id属性
    data.pop('id')
    db = mongoConnect()
    collection = db['filmInfo']
    # 查看数据库中有无此数据
    res = collection.find_one({'title':data['title']})
    # 存在，合并两个字段
    if res:
        res.pop('_id') 
        for k,v in data.items():
            # 判断键是否存在
            if k in res.keys():
                continue
            # 不存在，新增
            res[k] = v
        collection.delete_one({'title':res['title']})
        collection.insert_one(res)
        return
    # 不存在，插入
    date = data['release_date']
    if type(date) != 'str':
        data['release_date'] = date.strftime('%Y-%m-%d')
    collection.insert_one(data)       
        
# 数据库迁移
def migrate():
    data = getMysqlFilmInfo()
    # 对事件类型做修改
    for i in data:
        o = i['release_date']
        if type(o) == str:
            continue
        o = o.strftime('%Y-%m-%d')
        i['release_date'] = o
        # 删除id字段
        i.pop('id')
    saveMongo(data)
# 数据库合并
def merge():
    data = getMysqlTMDB()
    for i in data:
        mongoUpdate(i)
    
migrate()
merge()
    