# 爬虫
import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import connect
# 请求头
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Cookie":"ll='118259'; bid=eqGee7kS9EU; __gads=ID=505d6ca95581ef53-2289b8380cd80001:T=1667480608:RT=1667480608:S=ALNI_Mbc5NgNL4oHCbnTsxuluvv4XK3GyQ; _vwo_uuid_v2=D0E40BFA56A7332245A9FADABFF651FD8|1ba735ee40d79ebd8fa7c5bba2712585; gr_user_id=ac7b0e07-3e54-4a92-9171-91f53f0178e7; viewed='27204133_27015617'; __utmc=30149280; dbcl2='259081538:08f00dsqiQQ'; ck=LdXy; __gpi=UID=00000b74567f9c91:T=1667480608:RT=1677494612:S=ALNI_MbaR_9_913Cg4TaAJlpxlhZvN1xDA; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25908; __utmc=223695111; __yadk_uid=MqQD11piFB7gxJH8Kir49jqkqmEvM3zq; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1677494619; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1677494619; frodotk_db='3ad2134b8fe12cceb07639e2afa3866a'; __utmz=30149280.1677499522.7.7.utmcsr=jobs.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1677499522.6.6.utmcsr=jobs.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=["","",1677502918,'https://jobs.douban.com/']; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.26488797.1667480608.1677499522.1677502918.8; __utmb=30149280.0.10.1677502918; __utma=223695111.754254544.1667480608.1677499522.1677502918.7; __utmb=223695111.0.10.1677502918; _pk_id.100001.4cf6=124122e1b4fa613a.1667480608.7.1677503054.1677499560."
}

# 爬取排行榜数据
# 基本网址
base_url = "https://movie.douban.com/chart"
# 分类排行榜的基础接口
classify_url = "https://movie.douban.com/j/chart/top_list"
# 用来接收分类的列表
classify_List:list[int] = []

# 获取分类列表
def getClass()->list[int]:
    response = requests.get(base_url,headers=header)
    soup = BeautifulSoup(response.text,'lxml')
    print(soup.text)
    types = soup.select('.types a')
    for i in types:
        classify_List.append(int(i["href"].split("&")[1].split("=")[1]))
    return classify_List

# 获取每个分类排行榜的数据总数
def getInfo(type:int)->int:
    total = requests.get("https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100:90".format(type),headers=header)
    return json.loads(total.content)['total']


# 获取一个分类下的所有数据
def getOwn(type:int)->list[dict]:
    # 存储分类数据
    ownList:list[dict] = []
    # 获取分类电影的总数
    total = getInfo(type)
    for i in range(0,total,20):
        res = requests.get("https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20".format(type,i),headers=header)
        print(res.content)
        ownList.extend(json.loads(res.content))
        sleep(random.randint(0,3))
    return ownList

# 获取一个电影的评论
def getComment(id:int)->dict:
    # 接收评论数据及好评差评概率
    str = ''
    d = {}
    html = requests.get("https://movie.douban.com/subject/{}/comments?status=P".format(id),headers=header)
    bs4 = BeautifulSoup(html.text,'lxml')
    # 获取好评率
    l = bs4.select(".comment-percent")
    d['favourable'] = int(l[1].text.split("%")[0])
    d['general'] = int(l[1].text.split("%")[0])
    d['differ'] = int(l[1].text.split("%")[0])
    for i in range(5):
        sleep(random.randint(0,3))
        # 获取网页
        html = requests.get('https://movie.douban.com/subject/{}/comments?start={}&limit=20&status=P&sort=new_score'.format(id,i),headers=header)
        bs4 = BeautifulSoup(html.text,'lxml')
        for i in bs4.select(".short"):
            str += i.text + "\n"
    d['str'] = str
    return d
getOwn(31)