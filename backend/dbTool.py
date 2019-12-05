
import sys,os 
sys.path.append(os.getcwd())
from backend.create_table import zhihuTables
from backend.create_table import Session
import time
from datetime import datetime, timedelta
from collections import Counter
from backend import config
from sqlalchemy import func ,extract, update, inspect 

class dbTool(object):
    def __init__(self):
        self.sqlite_session = Session()

    def insert_item(self, item):
        # print('inset_item()')
        # print(item['created_time'])
        dateT = datetime.utcfromtimestamp(int(item['created_time']))
        # 一定要采用以下标准格式
        date = dateT.strftime('%Y-%m-%d %H:%M:%S')
        # date = datetime(dateT)
        # date = datetime(int(item['created_time']))
        # print(date)
        data = zhihuTables(
            articleId= item['id'],
            authorName = item['author']['name'],
            authorId= item['author']['url_token'],
            followers= item['author']['follower_count'],
            createTime = item['created_time'],
            createDate = date,
            vote = item['voteup_count'],
            content = item['content'] 
        )
        # 在存储数据 之前，查询一下是否有这条回答
        try:
            query_result = self.sqlite_session.query(zhihuTables.articleId, zhihuTables.vote).filter(zhihuTables.articleId == item['id']).first()
        #  
        except:
            return     
        print(query_result)
        if not query_result: 
            try:
                self.sqlite_session.add(data)    
                self.sqlite_session.commit()
                print('新增文章%s'%item['author']['name'])
            except:
                self.sqlite_session.rollback()
                print("新增文章，插入数据库失败") 
                raise          
        elif query_result[1] != item['voteup_count'] :
            try:
                # self.sqlite_session.query().filter(zhihuTables.articleId == item['id']).update({
                #     'vote' : item['voteup_count']
                # })
                update(zhihuTables).where(zhihuTables.articleId == item['id']).values(vote=item['voteup_count'])
                self.sqlite_session.commit()
                print("该答案点赞数增加了")
            except:
                self.sqlite_session.rollback()
                print("更新点赞，插入数据库失败") 
                raise                     
        else:    
            print("该答案己存在%s:%s"%(item['id'], item['author']['name']))

 
            

    def query_vote(self):
        info = {}
        # 查询所有的点赞信息
        # 降序排列.desc()
        result = self.sqlite_session.query(zhihuTables.vote).order_by(zhihuTables.vote).all()
        # print(result)
        result_list = [x[0] for x in result]
        # print(result_list)
        counter_list = [x for x in Counter(result_list).items()]
        # 填充入serise 中的data 
        # 生成字典
        data = [{"name":x[0], "value":x[1]} for x in counter_list ]
        name_list = [item['name'] for item in data]
        info['x_name'] = name_list
        info['data'] = data  
        # print(info)
        return info

    # 查询排名前config.topTotal 的答案
    # 返回原始数据，在run.py中包装，减少数据量
    def query_topx(self):
        info = {}
        result = self.sqlite_session.query(zhihuTables.authorName ,zhihuTables.vote, zhihuTables.content).order_by(zhihuTables.vote.desc()).limit(config.topTotal).all()
        data = [{"name":x[0], "value":x[1],"content":x[2]} for x in result ]
        # name_list = [item['name'] for item in data]
        # info['x_name'] = name_list
        # info['data'] = data  
        # print(info)
        return data

    def query_byDay(self):
        info = {}
        # data_format 不适用于Sqlite

        # 通过query 检查生效情况
        # result = self.sqlite_session.query( func.hour(zhihuTables.createTime)).all() # 无hour() 函数
        # result = self.sqlite_session.query( extract('hour', zhihuTables.createTime)).limit(20).all() # 全是None
        # result = self.sqlite_session.query(func.strftime('%Y %m %d', zhihuTables.createDate)).limit(20).all() # 成功
        # 完整语句
        result= self.sqlite_session.query(func.strftime( '%Y-%m-%d',zhihuTables.createDate).label('day'), func.count('*').label('count')).group_by('day').all()
        data = [{"name":x[0], "value":x[1]} for x in result ]
        name_list = [item['name'] for item in data]
        info['x_name'] = name_list
        info['data'] = data  
        # print(info)
        return info

    # 计算总赞数
    def query_votesum(self): 
        result = self.sqlite_session.query(func.sum(zhihuTables.vote)).first()
        # print(result)
        return result[0]

    def query_byId(self, id):
        result = self.sqlite_session.query(zhihuTables.authorName, zhihuTables.vote, zhihuTables.content).filter(zhihuTables.id == id).first()
        return result 

    def query_byTop(self, i):
        subquery = self.sqlite_session.query(
            zhihuTables.authorName,
            func.rank().over(
                order_by = zhihuTables.vote.desc()
            ).label('rnk')
        ).subquery()
        result = self.sqlite_session.query(subquery).filter(
            subquery.c.rnk == 1
        )

        # result = self.sqlite_session.query(zhihuTables.authorName, zhihuTables.vote, zhihuTables.content).func.rank(i).over(order_by='vote')
        # print(result)
        return result         


zhihu_sqlTool = dbTool() 
# zhihu_sqlTool.query_byDay()
# zhihu_sqlTool.query_topx()
# zhihu_sqlTool.query_vote()
# print(zhihu_sqlTool.query_byId(1))
# zhihu_sqlTool.query_votesum()
# zhihu_sqlTool.query_byTop(1)
