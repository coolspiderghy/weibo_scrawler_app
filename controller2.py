# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Queue
import time
import csv
import logging

import config
from crawler.blogcrawler import BlogCrawler, UserNotFoundError, PreprocessError
from crawler.toolkit import filelib as fl
from crawler.toolkit.accountlib import AccountManager
from crawler.usercrawler import UserCrawler
from unslib import *

class Controller(object):
    """
    爬虫程序，负责抓取数据并保存
    """
    taskpool = Queue.Queue()  # 任务池
    finished_count = 0  # 已完成的任务数
    unexist_user_writer = None  # 不存在的用户的写入器
    noblog_user_writer = None  # 没有合法微博的用户的写入器

    @classmethod
    def load_tasks(cls,uns):
        """
        生成任务，类方法，不能通过类的实例来调用。
        通过类名来调用，整个程序运行过程中只执行一次。
        """
        # 加载需要过滤的用户列表
        #finished_uns=open('completes.txt').read().strip().split()
        # 加载需要执行的任务
        print u'共', len(uns)
        for un in uns:
            #if un not in finished_uns:
            cls.taskpool.put(un)

    @classmethod
    def init(cls,uns):
        """
        执行程序前初始化，包括加载任务，初始化写入器，模拟登录等
        --------------------------------------------
        return: 初始化成功返回True，否则返回False
        """
        success = True
        # 进行模拟登录
        account_manager = AccountManager()
        try:
            while True:
                account_manager.init()
                if not account_manager.login():
                    print u'开始重新登录...'
                else:
                    break
        except Exception, e:
            print '模拟登录失败!', str(e)
            return False
        cls.load_tasks(uns)
        cls.unexist_user_writer = open(config.UNEXIST_USER_FILEPATH, 'a')
        cls.noblog_user_writer = open(config.NOBLOG_USER_FILEPATH, 'a')
        return True

    @classmethod
    def free(cls):
        """
        程序执行结束以后释放资源
        """
        cls.unexist_user_writer.close()
        cls.noblog_user_writer.close()

    @classmethod
    def let_us_go(cls,uns):
        """
        启动程序，包括初始化，实例化线程，以及结束以后的资源释放
        ----------------------------------------------
        thread_count: 工作线程的数量
        """
        cls.init(uns)
        Controller().run()

    def run(self):
        """
        多线程的入口函数
        """
        crawler = BlogCrawler()
        #crawler = UserCrawler()
        while not Controller.taskpool.empty():
            un = Controller.taskpool.get()
            print "\n已处理 %d 个任务, 还剩 %d 个任务" % (Controller.finished_count, Controller.taskpool.qsize())
            #print uns
            try:
                urls=get_urls(get_uns_uids(config.UID_FILEPATH)[1])
                uns=get_uns_uids(config.UID_FILEPATH)[0]
                #print urls,'testing........'
		print 'task start'
                #userinfo_dic={'username':userid}
                #url = 'http://weibo.com/u/1340714021'
                #url='http://weibo.com/u/1756439121'
                #url = 'http://weibo.com/caikangyong'
                #url = 'http://weibo.com/u/1704116960'
                #url = 'http://weibo.com/u/1730336902'
                #userinfo = crawler.scratch(un)
                #Controller.save_userinfo(userinfo,un)
                print 'crawlering %s th bloger....'%(uns.index(un)+1)
                blogs = crawler.scratch(urls[uns.index(un)])
                Controller.save_csv(blogs, un)
		print 'task end'
            except:
                print un
            Controller.finished_count += 1
    @staticmethod
    def save_userinfo(userinfo,un):
        #with open('fuid.txt', 'a') as f:
        #    for fuid, un ,an ,follow_num,fans_num,weibo_num in userinfo['fui']:
        #        f.write(str(uid)+'\t'+str(fuid)+'\t'+un+'\t'+an+'\t'+str(follow_num)+'\t'+str(fans_num)+'\t'+str(weibo_num)+'\n')
        #with open('followee.txt', 'a') as f:
         #   for fuid,un,an ,a,b,c in userinfo['fui']:
         #       f.write(str(fuid)+'\n')
         #       f.write('\n')
        with open('user_repost.txt','a') as f:
            #print 'test.....',userinfo['fui']
            for follow in userinfo['fui']:
                print 'follower.....',str(un)+'\t'+follow[0]+'\t'+follow[1]+'\t'+follow[2]+'\t'+follow[3]+'\n'
                f.write(str(un)+'\t'+follow[0]+'\t'+follow[1]+'\t'+follow[2]+'\t'+follow[3]+'\n')
        with open('user_2_repost.txt','a') as f:
            for follow_2 in userinfo['2_fui']:
                f.write(follow_2[0]+'\t'+"\t".join(follow_2[1])+'\n')
        with open('completes.txt','a') as f:
            f.write(str(un)+'\n')    
        with open('uun.txt','a') as f:
            for follow in userinfo['fui']:
                if not isInuun(follow[1]):
                    f.write(follow[1]+'\t'+follow[0]+'\n')    
    @staticmethod
    def save_csv(blogs, un):
        """
        将一组微博写到CSV文件中
        ---------------------------------
        blogs: 微博列表
        writer: 写入器
        """
        for blog in blogs:
            for b in blog:
                if blog[b]=='':
                    if b=='rrc' or b=='rc' or b=='rcc':
                        blog[b]=0
                    else:
                        blog[b]='NULL'
        #print blogs.index('')#blogs[blogs.index('')]='NULL'
        filename = Controller._get_filepath(un)
        writer = csv.writer(file(filename, 'w'))
        writer.writerow(
            ['un', 'uid', 'iu', 'mid', 'mc', 'srn', 'run', 'ruid', 'rmc', 'pu', 'rrc', 'rcc', 'rpage', 'rpt', 'rc',
             'cc', 'page', 'pt'])
        for blog in blogs:
            writer.writerow((blog['un'], blog['uid'], blog['iu'], blog['mid'], blog['mc'], blog['srn'],
                             blog['run'], blog['ruid'], blog['rmc'], blog['pu'], blog['rrc'], blog['rcc'],
                             blog['rpage'], blog['rpt'], blog['rc'], blog['cc'], blog['page'], blog['pt']))
        print u'用户', un, u'的微博已成功写入文件:', filename

    @staticmethod
    def _get_filepath(un):
        """
        获取文件的保存路径
        -------------------------
        return: 保存的路径
        """
        dirpath = config.dir_root + str(config.dir_count)
        if not fl.exists(dirpath):
            fl.create_dir(dirpath)
        if not fl.exists(os.path.join(dirpath, un + '.csv')):
            if fl.count(dirpath) >= config.MAX_FILE_COUNT:
                config.dir_count += 1
                dirpath = config.dir_root + str(config.dir_count)
                fl.create_dir(dirpath)
        return os.path.join(dirpath, un + '.csv')
