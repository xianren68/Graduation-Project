from . import models,ciyun
from django.http import JsonResponse,HttpResponse
from utils import error
from . import analysis
from . import mongo

# Create your views here.

# 返回排行榜数据
def reqBox(request):
    data = {}
    data['list'] = []
    l = models.getBoxTop()
    for i in l :
        d = {}
        d.update(i.__dict__)
        d.pop('_state')
        d.pop('id')
        data['list'].append(d)
    
    data['code'] = 200
    data['msg'] = error.getMsg(200)
    return JsonResponse(data)  
# 返回词云图
def resCiyun(request):
    name = request.GET.get('name')
    res = ciyun.ciyun(name)
    code = 200
    if res == '':
        code = 2001
    # 获取评论数据并转化为字典
    r = models.getComment(name)
    print(r.__dict__)
    d ={}
    d.update(r.__dict__)
    d.pop('_state')
    d.pop('id')
    data = {}
    data['code'] = code
    data['msg'] = error.getMsg(code)
    data['path'] = res
    data['precent'] = d
    return JsonResponse(data)
# 返回类型占比
def resTypeProportion(request):
    data = {}
    types = analysis.getTypes()
    data['types'] = types
    data['code'] = 200
    data['msg'] = error.getMsg(data['code'])
    return JsonResponse(data)   
# 返回推荐电影
def resRecommend(request):
    res = {}
    res['code'] = 200
    line = mongo.getRandom().content
    res['msg'] = error.getMsg(200)
    # if "--" in line:
    res['line'] = line
    # else:
    #     res['line'] = models.getRandom()
    return JsonResponse(res)
# 返回历年电影票房排行
def resYearTop(request):
    year = int(request.GET.get('year'))
    res = {}
    l = analysis.getCalenderTop(year)
    res['data'] = l
    res['code'] = 200
    res['msg'] = error.getMsg(200)
    return JsonResponse(res,safe=False)
# 返回首页推荐
def resHome(request):
    res = {}
    res['code'] = 200
    res['msg'] = error.getMsg(200)
    res['data'] = mongo.getRandom()
    return JsonResponse(res)
# 返回类型和盈利
def resTandP(request):
    res = {}
    res['code'] = 200
    res['msg'] = error.getMsg(200)
    res['data'] = analysis.getTandP(mongo.getProfit())
    return JsonResponse(res)
# 返回类型和评分
def resTandG(request):
    res = {}
    res['code'] = 200
    res['msg'] = error.getMsg(200)
    res['data'] = analysis.getTandG(mongo.getScore())
    return JsonResponse(res)
# 返回国家数量
def resYCount(request):
    res = {}
    res['code'] = 200
    res['msg'] = error.getMsg(200)
    res['data'] = analysis.countryYear(mongo.getAll())
    return HttpResponse(JsonResponse(res))
# 返回搜索电影
def resSearch(request):
    res = {}
    res['code'] = 200
    res['msg'] = error.getMsg(200)
    res['data'] = mongo.search(request.GET.get('name'))
    return HttpResponse(JsonResponse(res))