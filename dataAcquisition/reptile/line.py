# 爬一些电影名句，用于随机返回给前端
import requests
from bs4 import BeautifulSoup
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import connect
base_url = "https://kckdi.com/5055.html"
def get_movie_name():
    html = requests.get(base_url).content
    bs = BeautifulSoup(html,'lxml')
    pList = bs.select('.article-content p')
    res = []
    for i in range(1,len(pList)-1):
        s = pList[i].text
        # 去除序号
        s = s.split("、")[1]
        # # 去除书名号
        s = s.replace('《','')
        s = s.replace('》','')
        r = (s,)
        res.append(r)
    s = pList[len(pList)-1].text
    # # 去除书名号
    s = s.replace('《','')
    s = s.replace('》','')
    s = s[3:]
    r = (s,) 
    res.append(r) 
    connect.saveLine(res)
