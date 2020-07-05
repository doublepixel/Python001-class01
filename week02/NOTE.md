学习笔记

### 1、异常
```python
try:
    1/0
except Exception as e:
    print(e)
raise 

# list index out of range
# division by zero

```
用户自定义异常
```python
class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    del userinput
```

### 2、pymysql
```shell script
mysql.server start
ps -ef |grep mysql

pip install pymysql

# 一般流程
# 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束


# 无log 执行
scrapy crawl maoyao_spider --nolog

```







