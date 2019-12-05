
from flask import Flask, render_template, jsonify
# import os,sys,inspect
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir) 
# import sys
# sys.path.insert(0,'..')
import sys,os ,json
sys.path.append(os.getcwd())
from backend.dbTool import zhihu_sqlTool
from backend import config


# 实例化flask
app = Flask(__name__)

# 注册路由
@app.route("/")
def index():
    return "Hello World"

# get the data from sqlite, and feed it to ajax
@app.route("/fetch_echart_data")
def fetch_echart_data():
    info = {}
    # 直方图 x轴为种类
    # print("fetch_echart_data")
    # 从temp.json 或者数据
    with open(config.jpath,'r') as f:
        temp = json.load(f)
    # 将json中的数据传给前端
    # print(temp)
    info['json'] = temp
    # info['topx'] = topx
    # 从数据库获得数据
    data = zhihu_sqlTool.query_vote()
    vote_sum = zhihu_sqlTool.query_votesum()
    info['vote_sum'] = vote_sum

    
    # 将前n名的数据传给前端ajax
    topx = zhihu_sqlTool.query_topx()
    # 最前几项，显示高票答主
    info['echart_2'] = {
        'x_name' : topx['x_name'][:config.top],
        'data' :topx['data'][:config.top]
    }

    # 点赞数量分析,折线图
    info['echart_4'] = data
    # 回答随时间数据分析
    answers = zhihu_sqlTool.query_byDay()
    # print(answers)
    info['echart_5'] = answers

    # 取答案传给前端
    # answer = zhihu_sqlTool.query_byId(1)
    info['answer'] = topx


    # info['map'] = data
    # print(info)
    # print("this is info echart_4")
    # print(info['echart_4'])
    return jsonify(info)

@app.route("/zhihu",methods=['GET','POST'])
def zhihu():
    # result = zhihu_sqlTool.query_vote()
    # return render_template('index.html',result=result)
    return render_template('index.html')

if __name__ == '__main__':
    # 启动flask
    # import sys, os 
    # sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
    # from backend.dbTool import zhihu_sqlTool
    # import sys 
    # sys.path.append("..")
    app.run(debug = True)