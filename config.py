# !/usr/bin/python
#-*- coding: utf-8 -*-

import Queue
import threading
# from crawler.toolkit.dblib import DBManager

# 此文件用于定义一些全局变量

# 数据库配置信息 #
# server = '219.223.244.121'
# user = 'root'
# pwd = 'hiticrc'
# database = 'graduation'

# db = DBManager(server, user, pwd, database)

THREAD_COUNT = 1
EACH_MACHINE_TASK_COUNT = 3000
MACHINE_ID = 0

# 全局变量
finished_tasks = set()  # 已完成的任务集合

# 保存非法用户文件
UNEXIST_USER_FILEPATH = 'log/unexist-user.txt'
NOBLOG_USER_FILEPATH = 'log/noblog-user.txt'

# 文件保存设置
dir_count = 0  # 计数当前目录编号
dir_root = '/Users/genghaiyang/ghy_works/projects/weibo_crawler/data/blogcontents'  # 保存文件的根目录
MAX_FILE_COUNT = 1000  # 每个文件夹最多保存的文件数目

# 用户ID存放地址
UID_FILEPATH = 'uun.txt'

# 抓取的数据的时间间隔
begin_time = '2010-1-1 00:00:00'
end_time = '2016-12-30 00:00:00'