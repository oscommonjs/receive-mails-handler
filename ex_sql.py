#!/usr/bin/env python
# coding=utf-8
import MySQLdb
import sys
import config
'''
    功能: 1. 更新数据库模块, 可单独运行 2. 查询数据库状态
    命令:   1. python ex_sql.py u 版权hash 例: python ex_sql.py u b646554d75632a80d30a39bf1fa00c0757ebbea6
            2. python ex_sql.py sql命令 例: python ex_sql.py select hash from hash where 1 limit 1
'''
conn = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASS, db=config.DB_NAME, port=config.DB_PORT, charset='utf8')
cursor_remote = conn.cursor()
if sys.argv[1] == "u":
    # 接收显示出的第二个命令行参数，我这里是 设置type =9 即设置该链接为处理链接
    sql = "update hash set search_type = 9 where info_hash ='"+sys.argv[2]+"'"
else:
    sql = sys.argv
    del sql[0]
    sql = " ".join(sql)
print sql
count = cursor_remote.execute(sql)
fetch = cursor_remote.fetchall()
print fetch
