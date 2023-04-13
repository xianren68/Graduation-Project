from django.urls import path
from . import views
# 分发路由
urlpatterns = [
    path('login/',views.login),
    path('register/',views.register),

]