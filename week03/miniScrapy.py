import threading

import requests


class CrawlThread(threading.Thread):
    '''
    爬虫类
    '''
    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        """
        重写run 方法
        :return:
        """
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟任务调度
    def scheduler(self):
        while True:
            if self.queue.empty():
                break
            else:
                page = self.queue.get()
                print('下载线程：',self.thread_id, "下载页面：",page)
                url = f"https://book.douban.com/top250?start={page*25}"
                hreaders = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                }
                try:
                    # downloader
                    response = requests.get(url, headers=hreaders)
                    dataQueue.put(response.text)
                except Exception as e:
                    print("下载出现异常：",e)


class ParseThread(threading.Thread):
    """
    页面内容分析
    """
    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file =file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:
            try:
                item = self.queue.get(False)
                if not item:
                    continue
                self.parse_data(item)
                self.queue.tash_done()
            except Exception as e:
                pass
        print(f"结束线程：{self.thread_id}")

    def parse_data(self, item):
        """
        解析网页内容的函数
        :param item:
        :return:
        """
        try:
            html= etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title =