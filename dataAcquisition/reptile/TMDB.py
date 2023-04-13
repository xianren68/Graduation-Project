# 爬取TMDB的数据，用于电影推荐
import requests
from bs4 import BeautifulSoup
import sel
from time import sleep
import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import connect
# 请求头
header = {
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Cookie':'tmdb.prefs=%7B%22adult%22%3Afalse%2C%22i18n_fallback_language%22%3A%22en-US%22%2C%22locale%22%3A%22zh-CN%22%2C%22country_code%22%3A%22CN%22%2C%22timezone%22%3A%22Asia%2FShanghai%22%7D; OptanonAlertBoxClosed=2023-03-30T13:00:26.469Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+01+2023+22%3A52%3A59+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202301.1.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false&geolocation=CN%3BHB; tmdb.session=Ac_uyj3_dGWDPPznyriwcLRAN0jHeazV5MZrx-FuhzRfKYUiHEglSUiNWTQnTcxLQFz7oHDQlR7BEy0pu7mzTM14eK6RhTEGAIrL7smZWaB8asfgdItU6-F2Tln901idXNvTVQ4dEhT72yJ1rPFy4vfzcMvlZGcKfwuF94AAi7YDEzGoh5wBibF114SUQf215_i3zNpT90un5kzXC4iBJGS1mwtkaVkED9LBFSYCoJ5P; _ga=GA1.2.1533751719.1680417686; _gid=GA1.2.532501290.1680417686; _dc_gtm_UA-2087971-10=1',
    "Content-Type": "application/x-www-form-urlencoded"
}
# post请求参数
def req(page:int)->str:
  data = {
  "air_date.gte": "",
  "air_date.lte": "2023-10-02",
  "certification": "",
  "certification_country": "CN",
  "debug": "",
  "first_air_date.gte": "",
  "first_air_date.lte": "",
  "ott_region": "HK",
  "page": "2",
  "primary_release_date.gte": "",
  "primary_release_date.lte": "",
  "region": "",
  "release_date.gte": "",
  "release_date.lte": "2023-10-02",
  "show_me": "0",
  "sort_by": "vote_average.desc",
  "vote_average.gte": "0",
  "vote_average.lte": "10",
  "vote_count.gte": "300",
  "with_genres": "",
  "with_keywords": "",
  "with_networks": "",
  "with_origin_country": "",
  "with_original_language": "",
  "with_ott_monetization_types": "",
  "with_ott_providers": "",
  "with_release_type": "",
  "with_runtime.gte": "0",
  "with_runtime.lte": "400"
    }
  data["page"] = str(page)
  return data
# 首页
base_url = "https://www.themoviedb.org"
FisrtTop = "https://www.themoviedb.org/movie/top-rated"
# 获取网址列表
def getList(page:int)->list:
    res = []
    # 判断是否在爬取第一页
    if page == 1 :
        response = requests.get(FisrtTop,headers=header)
    # 不是则为post请求
    else :
        print(page)
        data = req(page)
        response = requests.post('https://www.themoviedb.org/discover/movie/items',data=data,
                                    headers=header)
    soup = BeautifulSoup(response.text,'lxml')
    for i in soup.find_all(class_='card style_1'):
        x = i.select('a')[-1].attrs['href']
        res.append(x.split('/')[-1])
    return res

def save(page:int):
    l = getList(page)
    i = 0
    while i != len(l):
        data = sel.getInfo(l[i])
        # 超时重试
        if data == 0 :
            continue
        connect.saveTmdb(data)
        print(data['title'])
        sleep(2)
        i += 1   
for i in range(86,91):
    save(i)

# save(1)
# print(getList(4))