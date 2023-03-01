import pymysql
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import setting

# 创建数据库连接
def createConnect():
    db = pymysql.connect(host=setting.DbHost,port=setting.DbPort,user=setting.DbUser,
                     password=setting.DbPassWord,database=setting.DbName)
    return db

# 插入电影信息数据
def InsertInfo(data:dict)->None:
    data['types'] = ','.join(data['types'])
    data['actors'] = ','.join(data['actors'])
    data['regions'] = ','.join(data['regions'])
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into filmInfo(title,types,actors,score,release_date,regions,vote_count) values ('{}','{}','{}',{},'{}','{}',{})".format(data['title'],data['types'],data['actors'],data['score'],data['release_date'],data['regions'],data['vote_count'])
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

# 插入电影的好评率等
def InsertComment(data:dict):
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into comment(title,favourable,general,differ) values ('{}',{},{},{})".format(data['title'],data['favourable'],data['general'],data['differ'])
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

# 存入票房排行榜
def saveRank(data:dict):
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into boxOffice(id,name,date,types,direct,boxoffice) values ({},'{}',{},'{}','{}','{}')".format(data['order'],data['name'],data['date'],data['types'],data['direct'],data['boxoffice'])
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()