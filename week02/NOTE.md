学习笔记
```shell script
#学号: G20200389020419
#姓名: lvyz
#班级: 3班
#小组: 8组
#作业&总结链接: https://github.com/doublepixel/Python001-class01/tree/master/week02
```
删除本地分支：
    git branch -d dev
    

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

redis-cli
settings 制定IP地址的信息
```python
# redis信息
REDIS_HOST='127.0.0.1'
REDIS_PORT=6379

# Scheduler的QUEUE
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Requests的默认优先级队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# 将Requests队列持久化到Redis，可支持暂停或重启爬虫
SCHEDULER_PERSIST = True

# 将爬取到的items保存到Redis
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
```
piplines设置
```python
class ScrapyclusterPipeline:
    def process_item(self, item, spider):
        return item


#  redis 存储了item
#  bash$  redis-cli
#  redis> keys *
#  redis> type cluster:items
#  redis> lpop cluster:items
#  redis> keys *


```
