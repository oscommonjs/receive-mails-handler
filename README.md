# receive-mails-handler
借助Python3使用pop3协议收取服务器上的邮件，并实现自动化信息处理

## 应用
自动化处理磁力版权问题, 以及观测数据库状态

## 调用方式
### reveive_mails.py
主要处理文件
```
python3 receive_mail.py
```


### ex_sql.py
执行数据库语句

- 1. python ex_sql.py u 版权hash 
    例: `python ex_sql.py u b646554d75632a80d30a39bf1fa00c0757ebbea6`
- 2. python ex_sql.py sql命令 
    例: `python ex_sql.py select hash from hash where 1 limit 1`
