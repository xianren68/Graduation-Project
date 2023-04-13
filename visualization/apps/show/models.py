from django.db import models
import random
# 定义排行榜数据的模型
class BoxOffice(models.Model):
    name = models.CharField(max_length=50)
    date = models.IntegerField()
    types = models.CharField(max_length=50)
    direct = models.CharField(max_length=50)
    boxoffice = models.CharField(max_length=80)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'boxOffice'
# 定义评论数据模型
class Comment(models.Model):
    title = models.CharField(max_length=50)
    favourable = models.IntegerField()
    differ = models.IntegerField()
    general = models.IntegerField()
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'comment'
# 电影详情数据模型
class FilmInfo(models.Model) :
    title  = models.CharField(max_length=50)
    types =  models.CharField(max_length=200)
    actors =  models.CharField(max_length=500)
    score = models.FloatField()
    release_date = models.DateTimeField()
    regions = models.CharField(max_length=200)
    vote_count = models.IntegerField()
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'filmInfo'
# 电影推荐模型
class Recommend(models.Model):
    content=models.TextField()
    def __str__(self):
        return self.content
    class Meta:
        db_table = 'recommend'
# 获取排行榜数据
def getBoxTop():
    allData = BoxOffice.objects.all()
    return allData
# 获取评论数据
def getComment(name:str):
    data = Comment.objects.get(title=name)
    return data
# 获取电影类型行
def getTypes():
    data = FilmInfo.objects.values_list('types')
    return data

# 获取年份分组数据
def getDateNum():
    data = FilmInfo.objects.values_list('release_date')
    return data
# 获取随机的一个数据
def getRandom():
    count = Recommend.objects.count()
    print(count)
    rand = random.randint(0,count-1)
    return Recommend.objects.get(id=rand)
#