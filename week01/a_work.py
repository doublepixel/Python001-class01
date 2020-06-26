"""
作业一：
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""

import requests
# from lxml import etree
from bs4 import BeautifulSoup as bs
import pandas

class MaoYaoSpider:
    def __init__(self):
        self.url = r"https://maoyan.com/films?showType=3"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Pragma": "no-cache",
            "Host": "maoyan.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Cookie": 'uuid_n_v=v1; uuid=B0AF5F60B5B611EA95E3C92BBC8FF019A96EEF9A7E434DB382A16656A99567EC; _csrf=a886d660d68686bb489f21269122dc1db906e44109f530cdf8e13acf18f3355e; _lxsdk_cuid=172e3db1894c8-035685855ecf26-153e6554-384000-172e3db1894c8; _lxsdk=B0AF5F60B5B611EA95E3C92BBC8FF019A96EEF9A7E434DB382A16656A99567EC; mojo-uuid=986a4016b78b099a323042888bdc74c1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592960688; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593080972; __mta=154998279.1592960688989.1593080635592.1593080973917.9'
        }

    def send_request(self):
        response = requests.get(url=self.url, headers=self.headers)
        if response.status_code == 200:
            return response

    def parse_content(self, response):
        # bs4 处理html
        bs_info = bs(response.text, 'html.parser')
        movie_list = []
        for tags in bs_info.find_all('div', attrs={'class', 'movie-hover-info'})[0:10]:
            # 电影名称
            film_name = tags.find('span', {'class', 'name'}).get_text(strip=True)
            for i, attrs in enumerate(tags.find_all('div', attrs={'class', 'movie-hover-title'})):
                if i == 1:
                    # 电影类型
                    type = attrs.contents[-1].strip()
                if i == 3:
                    # 上映时间
                    date = attrs.contents[-1].strip()

            movie_list += [(film_name, type, date)]
        return movie_list

    def write_csv(self,content):
        work01_movie = pandas.DataFrame(content)
        work01_movie.to_csv('./work01_movie.csv', encoding='utf8', index=False, header=False)

    def start(self):
        response = self.send_request()
        if response:
            content = self.parse_content(response)
            self.write_csv(content)



if __name__ == '__main__':
    mys = MaoYaoSpider()
    mys.start()
