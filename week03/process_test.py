
from multiprocessing import Process, Value, Array


# from multiprocessing import Process,Pipe
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__=="__main__":
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     p.join()
# p9
# from multiprocessing import Process,Queue
# import os,time
#
# def write(q):
#     print("启动Write子进程： %s" % os.getpid())
#     for i in ["A", "B", "C", "D"]:
#         q.put(i)
#         time.sleep(1)
#     print("结束Write子进程： %s" %os.getpid())
#
# def read(q):
#     print("启动Read子进程：%s" % os.getpid())
#     while True:
#         value = q.get(True)
#         print(value)
#     print("结束Read子进程：%s" % os.getpid())
#
# if __name__=="__main__":
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()
#     print("父进程结束")
# p8
# from multiprocessing import Process, Queue
# def f(q):
#     q.put([42, None, 'hello'])
#
# if __name__=="__main__":
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()
# p7
# from multiprocessing import Process
# from time import sleep
#
# num = 100
#
# def run():
#     print("子进程开始")
#     global num
#     num += 1
#     print(f'子进程num：{num}')
#     print("子进程结束")
#
# if __name__=="__main__":
#     print("父进程开始")
#     p = Process(target=run)
#     p.start()
#     p.join()
#     print("父进程结束。num: %s"% num)
#
# p6
# import os
# import time
# from multiprocessing import Process
#
# class NewProcess(Process):
#     def __init__(self,num):
#         self.num = num
#         super().__init__()
#
#     def run(self):
#         while True:
#             print(f"我是进程{self.num} ,我的pid是：{os.getpid()}")
#             time.sleep(1)
#
# for i in range(2):
#     p = NewProcess(i)
#     p.start()
