from database import connect
from reptile import DoubanTop
from reptile import storage
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def start():
    # 获取所有的类别
    classify = DoubanTop.getClass()
    # 遍历获取每一类
    for i in range(len(classify)):
        try:
            getClass(classify[i])
        except:
            # 重新爬
            time.Sleep(60*60*24)
            i-=1
            continue
        print("爬完了一个类")

# [11, 24, 5, 13, 17, 25, 10, 19, 20, 1, 23, 6, 14, 7, 28, 8, 2, 4, 22, 3, 27, 16, 15, 12, 29, 30, 18, 31]
def getClass(i:int):
    # 每个分类的电影列表
        infoList = DoubanTop.getOwn(i)
        for j in infoList:
            # 如果已经存在，直接下一条
            if connect.isExistInfo(j):
                continue
            # 获取评论信息
            comment = DoubanTop.getComment(int(j['id']))
            # 存储评论信息
            storage.saveComment(j['title'],comment['str'])
            # 存储数据到数据库
            try:
                connect.InsertInfo(j)
                comment['title'] = j['title']
                connect.InsertComment(comment)
            except Exception as e:
                print(j['title'],"存储出错",e)