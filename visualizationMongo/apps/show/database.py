# 一些原生的数据库操作
import pymysql
import pandas as pd
# 连接数据库
def createConnect():
    db = pymysql.connect(host="81.70.27.234", port=3306, user="root",
                         password="010825lwj", database="Graduation")
    return db
# 获取某年的票房数据
def getCalendar(year:int)->tuple[tuple]:
    db = createConnect()
    cursor = db.cursor()
    sql = "select * from {}boxOffice".format(year)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    return data

    db = createConnect()
    sql = "select release_date,regions from filmInfo"
    data = pd.read_sql(sql,db)
    db.close()
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