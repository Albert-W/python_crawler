
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
    print(temp)
    info['json'] = temp
    
    # 从数据库获得数据
    data = zhihu_sqlTool.query_vote()
    info['echart_1'] = data
    # 薪资发布数量分析
    info['echart_2'] = data 
    # 岗位数量分析,折线图
    info['echart_4'] = data
    #工作年限分析
    info['echart_5'] = data
    # #学历情况分析
    # info['echart_6'] = data
    # #融资情况
    # info['echart_31'] = data
    # #公司规模
    # info['echart_32'] = data
    # #岗位要求
    # info['echart_33'] = data
    #各地区发布岗位数
    info['map'] = data
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