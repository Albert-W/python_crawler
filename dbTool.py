from create_table import zhihuTables
from create_table import Session
import time
from datetime import datetime

class dbTool(object):
    def __init__(self):
        self.sqlite_session = Session()

    def insert_item(self, item):
        # print('inset_item()')
        # print(item['created_time'])
        dateT = datetime.utcfromtimestamp(int(item['created_time']))
        date = dateT.strftime("%Y %m %d %H:%M:%S")
        print(date)
        data = zhihuTables(
            articleId= item['id'],
            authorName = item['author']['name'],
            authorId= item['author']['url_token'],
            followers= item['author']['follower_count'],
            createTime = date ,
            vote = item['voteup_count'],
            content = item['content'] 
        )
        # 在存储数据 之前，查询一下是否有这条回答
        query_result = self.sqlite_session.query(zhihuTables).filter(zhihuTables.articleId == item['id']).first()

        if query_result:
            print("该答案己存在%s:%s"%(item['id'], item['author']['name']))
        else:
            self.sqlite_session.add(data)    
            self.sqlite_session.commit()
            print('新增文章%s'%item['author']['name'])

zhihu_sqlTool = dbTool() 