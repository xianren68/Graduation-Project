import jieba
import os
from wordcloud import WordCloud
from utils import encryption
comment_url = "./static/comment/"
img_url = "./static/ciyun/"


# 返回词云图地址
def ciyun(name:str)->str:
    # 判断是否有此电影的评论数据
    if not os.path.exists(comment_url+name+'.txt'):
        return ''
    e = encryption.encryption(name)
    path = img_url+e+".png"
    # 判断是否已经生成过了
    if os.path.exists(path):
        return path.replace(".",'',1)
    else:
        createCiyun(name,path)
        return path.replace(".",'',1)
# 生成词云图
def createCiyun(name,path)->str:
    txt = getComment(name)
    words = jieba.lcut(txt)     #精确分词
    newtxt = ''
    # 去除单字
    for i in words:
        if len(i)<2:
            continue
        else:
           newtxt = newtxt + '/' + i 
    
    wordcloud = WordCloud("./utils/钟齐志莽行书.ttf",height=200,width=400,background_color="white",mode="RGBA",scale=20).generate(newtxt)
    wordcloud.to_file(path)  
    
def getComment(name:str)->str:
    with open(comment_url+name+".txt","r",encoding='utf-8') as f:
        s = f.read()
        return s