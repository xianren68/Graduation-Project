from django.urls import path
from . import views
# 分发路由
urlpatterns = [
    path('boxoffice/',views.reqBox),
    path('ciyun/',views.resCiyun),
    path('types/',views.resTypeProportion),
    # path('year/',views.resDate),
    path('recommend/',views.resRecommend),
    path('yeartop/',views.resYearTop),
    path('home/',views.resHome),
    path('tandp/',views.resTandP),
    path('tandg/',views.resTandG),
    path('cy/',views.resYCount),
    path('search/',views.resSearch)
]