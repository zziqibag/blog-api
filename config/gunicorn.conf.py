import logging
import multiprocessing
import os
import time
from logging.handlers import WatchedFileHandler

bind = "0.0.0.0:8000"  # 绑定的ip与端口
# 以守护进程的形式后台运行
# daemon = True

backlog = 512  # 监听队列
timeout = 30  # 超时
worker_class = 'gevent'  # 使用gevent模式，还可以使用sync 模式，默认的是sync模式

workers = 2  # 进程数
# 启动的进程数
# workers = multiprocessing.cpu_count() * 2 + 1
threads = 1  # 指定每个进程开启的线程数

loglevel = 'info'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
proc_name = 'blog-api'  # 进程名

access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

"""
其每个选项的含义如下：
h          remote address
l          '-'
u          currently '-', may be user name in future releases
t          date of the request
r          status line (e.g. ``GET / HTTP/1.1``)
s          status
b          response length or '-'
f          referer
a          user agent
T          request time in seconds
D          request time in microseconds
L          request time in decimal seconds
p          process ID
"""

accesslog = "/dev/null"  # 访问日志文件的路径
errorlog = "/dev/null"  # 错误日志文件的路径

faccess = '{}.log'.format(time.strftime("%Y-%m-%d"))
ferror = '{}.log'.format(time.strftime("%Y-%m-%d"))


if os.environ.get('ENV', None):
    access_log_dir = '/data/logs/blog-api/access.{}'.format(faccess)
    error_log_dir = '/data/logs/blog-api/error.{}'.format(ferror)
else:
    access_log_dir = '/data/logs/blog-api/access.{}'.format(faccess)
    error_log_dir = '/data/logs/blog-api/error.{}'.format(ferror)

acclog = logging.getLogger('gunicorn.access')
acclog.addHandler(WatchedFileHandler(access_log_dir))
acclog.propagate = False
errlog = logging.getLogger('gunicorn.error')
acclog.addHandler(WatchedFileHandler(error_log_dir))
errlog.propagate = False
