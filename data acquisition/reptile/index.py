from database import connect
from reptile import DoubanTop
from reptile import storage
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def start():
    # 获取所有的类别
    classify = DoubanTop.getClass()
    # 遍历获取每一类
    for i in classify:
        # 每个分类的电影列表
        infoList = DoubanTop.getOwn(i)
        for j in infoList:
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
        print("爬完了一个类",i)


