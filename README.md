# mini-taobao

这是一个用 Django 搭建的迷你淘宝项目，有列表展示，加入购物车，结算，用户登录界面。

## 技术栈
### python
### Django
### Ajax（GET， POST 请求）
### 数据库使用 SQLite
### 一点 html 和 css

## 安装
### 安装 python 3 (https://www.python.org/downloads/)
### 安装 pipenv (https://blog.csdn.net/Hanniel/article/details/94294155): 
  
   ```
   pip install pipenv
   ```
### 安装 git （https://git-scm.com/downloads）
### 下载本项目代码：
  ```
  git clone https://github.com/whcm-coding/mini-taobao.git
  ```
### 进入本地项目目录安装依赖：
  ```
  cd ./mini-taobao
  
  pipenv install（会在虚拟环境下安装 Django ）
  ``` 
### 进入虚拟环境命令行：
  ```
  pipenv shell
  ```
### 启动服务器
  ```
  python manage.py runserver
  ```
### 打开浏览器，在地址栏输入
  localhoost:8080