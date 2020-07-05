学习笔记

### 1、迭代器
```python
def chain(num):
    for it in range(num):
        yield it

num = 5 
y = chain(num)
next(y)     # 0
list(y)     # [1, 2, 3, 4]
next(y)     # StopIteration
```

### 常用列表推导式
```python
# 列表推导式
mylist2 = [i**2 for i in range(1, 11) if i > 5]

# 循环嵌套
mylist = [str(i) + j for i in range(1, 6) for j in 'ABCDE']

# 用推导式将字典转换为列表
mydict = {'key1': 'value1', 'key2': 'value2'}
mylist2 = [key + ':' + value for key, value in mydict.items()]

# 推导式生成字典
mydict = {i: i*i for i in (5, 6, 7)}

# 推导式实现字典的k-v互换
{value: key for key, value in mydict.items()}

# 推导式生成集合
myset = {i for i in 'HarryPotter' if i not in 'er'}

# 推导式生成 生成器
mygenerator = (i for i in range(0, 11))
print(mygenerator)
print(list(mygenerator))
```


### 3、scrapy

user_agent
```shell script
USER_AGENT_LIST=[
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
import random
USER_AGENT = random.choice(USER_AGENT_LIST)
```

跨域请求，调试
```shell script
yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
```

### 4、ajax局部数据动态获取
Asynchronous Javascript And XML  异步Javascript和XML，ajax实现了局部刷新效果，通过使数据和服务端 快速动态交互，不需要刷新及以及加载整个页面，对网页对某部分内容进行更新。
ajax有涉及到创建对象，发送接口请求，响应数据，结果判断等。
如JQuery的ajax：
```html
function savedata()
{
           var name = $('#name').val();
           var message = $('#message').val();
           $.ajax({
                url: "/savedata/",
                data:"name="+ name + "&message=" + message,
                headers:{'X-CSRFToken': '{{csrf_token }}'}, //csrf
                contentType:'application/x-www-form-urlencoded; charset=utf-8',
                type: "POST",
                success: function (result) {
                 //  console.log();
                },
                fail: function (result) {
                    debugger
                }
           });
       }

```