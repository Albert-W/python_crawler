from sqlalchemy import create_engine, Integer,String 
from backend.config import sqlPath
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

# 创建数据库的连接
engine = create_engine(sqlPath)
# 操作数据库
Session = sessionmaker(bind = engine)

# 声明一个基类
Base = declarative_base()

class zhihuTables(Base):
    # 表名称
    __tablename__ = 'zhihu_data'

    id = Column(Integer, primary_key = True, autoincrement = True)

    articleId = Column(Integer)

    authorName = Column(String(length = 32)) 

    authorId = Column(Integer) 

    followers = Column(Integer)

    createTime = Column(String(length=32))

    vote = Column(Integer)

    content = Column(String)

if __name__ == "__main__":
    # 创建数据表
    zhihuTables.metadata.create_all(engine)