import pandas
# from scrapy import log
import pymysql
import pymysql.cursors
import codecs
from twisted.enterprise import adbapi

import pymysql

from maoyan import settings


class PymysqlPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            db='django0115',
            user='root',
            passwd='root',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        cursor = self.cursor
        print(item['film_name'], item['film_type'], item['film_date'])
        sql = 'insert into maoyan01(name, type, date) values(%s, %s, %s)'
        cursor.execute(sql, (item['film_name'], item['film_type'], item['film_date']))
        self.connect.commit()
        return item


# class MaoyanPipeline:
#
#     # def process_item(self, item, spider):
#     #     """
#     #     将数据保存至csv文件中
#     #     :param item:
#     #     :param spider:
#     #     :return:
#     #     """
#     #     print(item.values())
#     #     work02_movie = pandas.DataFrame(item.values())
#     #     work02_movie.to_csv('./work02_movie.csv', mode='a', encoding='utf-8', index=False, header=False)
#     #     return item
#
#     @classmethod
#     def from_settings(cls, settings):
#         dbargs = dict(
#             host=settings['MYSQL_HOST'],
#             db=settings['MYSQL_DBNAME'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             port=settings['MYSQL_PORT'],
#             charset='utf8',
#             cursorclass=pymysql.cursors.DictCursor,
#             use_unicode=True,
#         )
#         dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
#         return cls(dbpool)
#
#
#     def __init__(self,dbpool):
#         self.dbpool=dbpool
#
#     #pipeline默认调用
#     def process_item(self, item, spider):
#         d=self.dbpool.runInteraction(self._conditional_insert, item, spider)#调用插入的方法
#         # log.msg("-------------------连接好了-------------------")
#         d.addErrback(self._handle_error,item,spider)#调用异常处理方法
#         d.addBoth(lambda _: item)
#         return d
#
#     def _conditional_insert(self, conn, item, spider):
#         # log.msg("-------------------打印-------------------")
#
#         conn.execute("insert into maoyan (name, type, date) values(%s, %s, %s)",
#                      (item['file_name'], item['film_type'], item['film_date']))
#         # log.msg("-------------------一轮循环完毕-------------------")
#
#     def _handle_error(self, failue, item, spider):
#         print(failue)
