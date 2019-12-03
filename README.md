# python_crawler
本项目旨要做一个轻量，易读，方便拓展的 知乎爬虫。 

设计之初就尽量避免引入额外的框架和数据库引擎，因此它是一个**python原生爬虫**，数据库采用的是最轻便的sqlLite.

为方便数据库与对象的映射， 引入了sqlalchemy， 此外没有其他包了。 

前置条件
```bash
pip install sqlalchemy
```

## 文件介绍
1. config.py 
所有的配置信息，都通过config.py 统一管理。 

通过修改config.py 可以拓展程序的功能。 

2. create_table.py
设计表结构，并通过ORM 在数据库中创建表 

3. dbTool.py
对数据库的操作，包装成python 函数。 

4. zhihu.py
全部爬虫功能实现

5. zhihu.db
保存爬虫信息的 sqlite数据库文件

6. frontend/
可视化展示的文件件，主要是前端文件  及 flask 路由



## 数据库设计

### 需要保存的字段

1. id 自增
2. 文章id   ['data']['id']
3. 用户名称  ['data']['author']['name']
4. 用户id    ['data']['author']['url_token']
5. 粉丝数   ['data']['author']['follower_count']
6. 创建时间  ['data'][created_time']
7. 点赞数    ['data]['voteup_count']
8. 内容  ['data]['content']

## 可视化设计

1. 随时间的发布聚类统计


2. 点赞数与文章量的统计
