# 爬取历年电影票房
import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import connect
base_url = 'http://www.boxofficecn.com/boxoffice'


def getData(year: int) -> list[dict]:
    response = requests.get(base_url+str(year))
    soup = BeautifulSoup(response.text, 'lxml')
    boxList = soup.select("tr")
    l = []
    for i in range(1, len(boxList)):
        d = {}
        try:
            d['year'] = int(boxList[i].select('td')[1].text)
            d['name'] = boxList[i].select('td')[2].text.split("（")[0]
            d['boxoffice'] = float(boxList[i].select('td')[3].text.split("（")[0])
        except:
            continue
        l.append(d)
    return l


def getOwnData():
    for i in range(2018, 2023):
        sleep(5)
        data = getData(i)
        print(data)
        connect.saveRankYear(i, data)
        print(i)


getOwnData()
