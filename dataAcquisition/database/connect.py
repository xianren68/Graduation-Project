from config import setting
import pymysql
import os
import sys
import json

# 创建数据库连接
def createConnect():
    db = pymysql.connect(host=setting.DbHost, port=setting.DbPort, user=setting.DbUser,
                         password=setting.DbPassWord, database=setting.DbName)
    return db
# 判断是否电影信息是否存在
def isExistInfo(data: dict) -> bool:
    db = createConnect()
    cursor = db.cursor()
    checkSql = "select * from filmInfo where title = '{}'".format(
        data['title'])
    if cursor.execute(checkSql):
        return True
    else:
        return False


# 插入电影信息数据
def InsertInfo(data: dict) -> None:
    data['types'] = ','.join(data['types'])
    data['actors'] = ','.join(data['actors']).replace("'", " ")
    data['regions'] = ','.join(data['regions'])
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into filmInfo(title,types,actors,score,release_date,regions,vote_count) values ('{}','{}','{}',{},'{}','{}',{})".format(
        data['title'], data['types'], data['actors'], float(data['score']), data['release_date'], data['regions'], data['vote_count'])
    cursor.execute(sql)
    print(data['title'])
    db.commit()
    cursor.close()
    db.close()

# 插入电影的好评率等


def InsertComment(data: dict):
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into comment(title,favourable,general,differ) values ('{}',{},{},{})".format(
        data['title'], data['favourable'], data['general'], data['differ'])
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

# 存入票房排行榜


def saveRank(data: dict):
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into boxOffice(id,name,date,types,direct,boxoffice) values ({},'{}',{},'{}','{}','{}')".format(
        data['order'], data['name'], data['date'], data['types'], data['direct'], data['boxoffice'])
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
# 存入名句


def saveLine(s: list):
    db = createConnect()
    cursor = db.cursor()
    sql = "insert into recommend(content) values(%s)"
    cursor.executemany(sql, s)
    db.commit()
    cursor.close()
    db.close()
# 历年票房排行榜


def saveRankYear(year: int, data:list[dict]):
    db = createConnect()
    cursor = db.cursor()
    isExistSql = "DROP TABLE IF EXISTS `{}boxOffice`".format(year)
    cursor.execute(isExistSql)
    db.commit()
    # 创建表
    vcreateSql = "\
    CREATE TABLE `{}boxOffice` (\
    `id` int(11) NOT NULL AUTO_INCREMENT,\
    `year` int(11) NOT NULL,\
    `name` varchar(255) NOT NULL,\
    `boxOffice` float NOT NULL,\
    PRIMARY KEY (`id`)\
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\
    ".format(year)
    cursor.execute(vcreateSql)
    db.commit()
    # 添加数据
    for i in data:
        sql = "insert into {}boxOffice(year,name,boxOffice) values ({},'{}',{})".format(year,i['year'],i['name'],i['boxoffice'])
        print(sql)
        cursor.execute(sql)
        db.commit()
    cursor.close()
    db.close()
    
 # 存入Tmdb数据
def saveTmdb(data:dict):
       db = createConnect()
       cursor = db.cursor()
       checksql = "select * from TMDB where title = '{}'".format(
        data['title'])
       # 若已存在
       if cursor.execute(checksql):
           return
       sql = "insert into TMDB\
       (title,release_date,types,grade,budget,boxoffice,runtime,line,introduction,background,cover) values\
           ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
               .format(data['title'],data['release_date'],data['types'],data['grade'],data['budget'],data['boxoffice'],data['runtime'],data['lines'].replace("'",'dou'),data['desc'].replace('“','').replace('”','').replace("'",''),data['background'],data['cover'])
       cursor.execute(sql)
       db.commit()
       cursor.close()
       db.close()
