# python_crawler
本项目旨要做一个轻量，易读，方便拓展的 知乎爬出。 

设计之初就尽量避免引入额外的框架和数据库引擎，因此它是一个知乎原生爬虫，数据库采用的是最轻便的sqlLite.

为方便数据库与对象的映射， 引入了sqlalchemy， 此外没有其他包了。 

前置条件
```bash
pip install sqlalchemy
```

## 配置清单

所有的配置信息，都通过config.py 统一管理。 

通过修改config.py 可以拓展程序的功能。 


## 数据库设计

### 需要保存的字段

# id 自增
# 文章id ['data']['id']
# 用户名称  ['data']['author']['name']
# 用户id ['data']['author']['url_token']
# 粉丝数 ['data']['author']['follower_count']
# 创建时间 ['data'][created_time']
# 点赞数 ['data]['voteup_count']
# 内容 ['data]['content']
