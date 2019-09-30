
# 详细操作步骤
___
## 安装pip：
  ### 卸载python
  ### 去官网下载安装包（https://www.python.org/）
  ### 选择 custom installation
## 在桌面新建文件夹 miniTaobao /
## 打开命令行cmd，输入 cd Desktop/
## 在cmd终端，输入:  cd miniTaobao/
## 在cmd终端，输入: pip install Django
## 输入 pip list，查看是否有Django，有才能继续下一步
## 在cmd终端，输入:  django-admin startproject miniTaobao
## 在cmd终端，输入:  python manage.py runserver
## 打开浏览器，在地址栏输入：http://127.0.0.1:8000/  确保能看到一个页面
___


## 在cmd终端，输入:  python manage.py startapp items
## 打开 items/views.py，把下面这些 Python 代码输入进去：
```
from django.http import HttpResponse
def index(request):
return HttpResponse(“你好！这是我的淘宝小项目！")
```
## 在 items 目录里新建一个 urls.py 文件（怎样新建文件参看第9次ppt：写一个真正有用的视图——显示我们的字典context）
## 在 items/urls.py 中，输入如下代码：
```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
```
## 在 miniTaobao/urls.py 输入：
```
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path(‘', include(items.urls'))]
```
## 刷新浏览器页面，能看到：你好！这是我的淘宝小项目！
___
	


