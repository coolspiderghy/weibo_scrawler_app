__author__ = 'Haiyang Geng'
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
import os
import csv
class Mysqldb(object):
    def __init__(self):
        self.ip='127.0.0.1'
        self.user='root'
        self.pwd= '100811'
        self.database='mydb'
        self.charset='utf8'
        self.con=mdb.connect('127.0.0.1','root','100811','mydb',charset='utf8')
    #(self.ip,self.user,self.pwd,self.database,self.charset)
    def mysqldb(self):
        self.__init__()
        try:
            self.cur =self.con.cursor()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)
        '''finally:
            if self.con:
                self.con.close()'''
if __name__ == '__main__':
    mysqldb_try=Mysqldb()
    mysqldb_try.mysqldb()
    #mysqldb_try.cur.execute("CREATE TABLE IF NOT EXISTS weibo_bloginfor (`un` varchar(255),`uid` varchar(255),`iu` varchar(255),`mid` varchar(255), `mc` varchar(255),`srn` varchar(255),`run` varchar(255), `ruid` varchar(255), `rmc` varchar(255), `pu` varchar(255), `rrc` varchar(255), `rcc` varchar(255),  `rpage` varchar(255), `rpt` varchar(255), `rc` varchar(255), `cc` varchar(255), `page` varchar(255), `pt` varchar(255));")
   # print mysqldb_try.cur.execute("select COLUMN_NAME from `information_schema`.`COLUMNS` where table_name = 'weibo_bloginfor' and table_schema = 'mydb';")
    #mysqldb_try.cur.execute("SET NAMES utf8mb4;")
    file_data_path='/Users/genghaiyang/ghy_works/projects/weibo_crawler/data/blogcontents/'
    files=os.listdir(file_data_path)
    
    for file_data in files[1:]:
        print file_data
        num=0
        for line in csv.reader(file(file_data_path+'/'+file_data,'rb')):
            if num==0:
                num=num+1
                continue
            else:
                #for i in range(1,16):
                mysqldb_try.cur.execute("insert into weibo_bloginfor VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17]))# for almost five hour, to figure out why the data can not be inserted into table. finally, search netwokr and find out is is about the commit()
                mysqldb_try.con.commit()
                num=num+1
    mysqldb_try.cur.close()
            