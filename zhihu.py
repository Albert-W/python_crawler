import requests
import config 
import re 
import time
import json
import multiprocessing
from dbTool import zhihu_sqlTool

class Crawlzhihu(object):
    def __init__(self):
        super().__init__()
        # 使用session 保存cookies信息
        self.zhihu_session = requests.session()
        self.header = {
            'User-Agent':config.useragent
        }
        self.pages = 0
    # 获取当前问题回答页码数
    def get_page(self):
        # 通过Xpath 查找想要的页码
        raw_result = self.handle_request(method='GET',  url=config.entry)
        # print(raw_result)
        # 使用正则表达式拿到列表
        pages_search = re.compile(config.regex)
        self.pages = int(pages_search.findall(raw_result)[0])
        # print(self.pages)

    # 获取某一页的数据
    def get_onepage(self, page):
        newUrl = config.answers_url.replace("offset=0","offset=" + str(20*page),1)
        # print(newUrl)
        raw_result = self.handle_request(method='POST', url=newUrl)
        # print(raw_result)
        json_data = json.loads(raw_result)
        # print(json_data)

        answers = json_data['data']
        # print(len(answers))
        for answer in answers:
            # print(answer)
            zhihu_sqlTool.insert_item(answer)
            time.sleep(0.01)
            # print(answer['author']['name'])
        # print(json_data)

    # 定义公用的请求信息
    def handle_request(self, method, url, data=None, info=None):

        if method == 'GET' or method == 'POST':
            response = self.zhihu_session.get(
                url=url,
                headers = self.header
            )
        return response.text    

if __name__ == "__main__":
    crawler = Crawlzhihu()
    # 获取页面数
    crawler.get_page()
    # 引入多进程，加快爬虫
    pool = multiprocessing.Pool(4)
    # 最后一页的下标为[crawler.pages-1]
    for i in range(0, crawler.pages ):
        print("this is page:" + str(i))
        pool.apply_async(crawler.get_onepage,args=(i,))
    pool.close()
    pool.join()    
    # crawler.get_onepage(3)