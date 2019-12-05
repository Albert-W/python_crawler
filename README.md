# python_crawler
本项目旨要做一个轻量，易读，方便拓展的 知乎爬虫。 

设计之初就尽量避免引入额外的框架和数据库引擎，因此它是一个**python原生爬虫**，数据库采用的是最轻便的sqlLite。 所有的定制信息都从config文件导入, 修改它可以实现定制功能。
 
## 效果展示

![image](zhihu_crawler.png)

## 前置条件
为方便数据库与对象的映射， 引入了sqlalchemy; 
为了提供网页服务器，采用了flask, 此外没有其他包了。

```bash
pip install sqlalchemy
pip install flask
```

## 文件介绍
### 根目录

1. zhihu.db
保存爬虫信息的 sqlite数据库文件

2. temp.json
保存不需要存入数据库的临时信息

### backend 
主要负责爬虫与持久化功能

1. config.py 
所有的配置信息，都通过config.py 统一管理。 修改config.py 可以拓展程序的功能。 

2. create_table.py
设计表结构，并通过ORM 在数据库中创建表。 

3. dbTool.py
对数据库的操作，包装成python 函数。 

4. zhihu.py
全部爬虫功能实现



### frontend
可视化展示的文件夹

1. templates/ 
提供了模版html, 是前端展示的入口

2. static/
包括图片，css, js 等资源文件

3. run.py
   
Flask 路由的实现，包括两个功能。

1 向前端传递json 数据

2 向前端传递展示页面。    


## 数据库设计

### 需要保存的字段

* id = Column(Integer, primary_key = True, autoincrement = True)
* articleId = Column(Integer)
* authorName = Column(String(length = 32)) 
* authorId = Column(Integer) 
* followers = Column(Integer)
* createTime = Column(String)
* createDate = Column(Text)
* vote = Column(Integer)
* content = Column(Text)

## 使用方法
1. 修改config.py , 输入想爬的网页，对应的正则表达式。 
2. 执行create_table.py, 会生成数据库以表单。 
3. 执行zhihu.py, 会爬取对应网页，并输入到数据库。默认：zhihu.db
4. 执行run.py, 启动网页服务器，通过浏览器访问。默认： http://127.0.0.1:5000/zhihu