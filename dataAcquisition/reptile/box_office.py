# 爬取票房前一百
import requests
from bs4 import BeautifulSoup
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import connect
base_url = "http://www.piaofang.biz/"
def getTop()->list[dict]:
    html = requests.get(base_url).content
    bs = BeautifulSoup(html,'lxml')
    # bs = bs.decode('utf-8')
    print(bs)
    tr = bs.select('tr')
    l = []
    for i in tr :
        if i.attrs == {'class' :['fenlei']} or i.attrs == {'class' :['space']} :
            continue
        if i.select('.title a'):
            name = i.select('.title a')[0].text
        else:
            name = i.select('.title')[0].text.replace('《',' ')
            name = name.replace('》',' ')
        d = {}
        d['order'] = i.select('.num')[0].text.split(" ")[-2]
        d['name'] = name
        d['date'] = i.select('.year')[0].text
        d['types'] = i.select('.type')[0].text
        d['direct'] = i.select('.daoyan')[0].text
        d['boxoffice'] = i.select('.piaofang span')[0].text
        l.append(d)
    return l
#
if __name__ == "__main__":
    for i in getTop():
        connect.saveRank(i)