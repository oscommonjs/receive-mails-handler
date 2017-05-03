# receive-mails-handler
借助Python3使用pop3协议收取服务器上的邮件，并实现自动化信息处理

## 应用
自动化处理磁力版权问题, 以及观测数据库状态

## 调用方式
### 主要处理文件
>reveive_mails.py

```
python3 receive_mail.py
```


### 执行数据库语句
>ex_sql.py

- `python ex_sql.py u notice_hahs`
     ```
     python ex_sql.py u b646554d75632a80d30a39bf1fa00c0757ebbea6
     ```
- `python ex_sql.py sql_command`
    ```
    python ex_sql.py select hash from hash where 1 limit 1
    ```

# 参考
http://blog.csdn.net/marksinoberg/article/details/66969620