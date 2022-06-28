# -*- coding:utf-8 -*-
import pymysql


class DB:
    # 数据库操作的上下文管理器
    def __init__(self,data_conf):
        self.conn = pymysql.connect(**data_conf)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()

DB_CONFIG = dict(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'mydb0804',
    port = 3306,
    charset = 'utf8'
)
with DB(DB_CONFIG) as cur:
    cur.execute('select * from emp;')
    print(cur.fetchall())