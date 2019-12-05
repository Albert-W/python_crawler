#  所有的配置入口

#  入口网页, 按时间排序
# 特点，无需要登录，也可以正常访问
entry = 'https://www.zhihu.com/question/306152036/answers/updated'
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 页码信息获取 的regex 
# 字串符匹配方式 对应 int(pages_search.findall(raw_result)[0])
# regex = r'ellipsis">...</button><button type="button" class="Button PaginationButton Button--plain">(.*?)</button>'
pRegex = r'ellipsis">...</button><button type="button" class="Button PaginationButton Button--plain">(\d+)</button>'

# 题目获取的regex 
tRegex = r'<title data-react-helmet="true">(.*?) - 知乎</title>'

# 题目描述的regex
cRegex = r'property="og:description" content="(.*?)"/><link'

# 回答数的regex 
ansRegex = r'itemProp="answerCount" content="(\d+)"/>'

# 问题的关注数regex
folRegex = r'zhihu:followerCount" content="(\d+)"/>'

# 总阅读数的regex
ReadRegex = r'"visitCount":(\d+),"'

# 获取具体数据的API地址
answers_url = 'https://www.zhihu.com/api/v4/questions/306152036/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=0&limit=20&sort_by=updated'

# sqlite 
sqlPath = 'sqlite:///zhihu.db'

# temporary file (json)
jpath = "temp.json"

# 收录前x x 高赞答主
topTotal = 200
# 显示前x x 答主
top = 7 


# Table name 
tableName = 'zhihu_data'