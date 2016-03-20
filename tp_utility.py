#-*-coding=utf-8-*-
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
def makeBlogFamework(path,filename):
    # this is for make framework for csv data
    import pandas as pd
    import mystats
    mystats.extendTime(path,filename)
    newfile = path+'/new_'+filename+'.csv'
    blog = pad.read_csv(newfile, header='infer', sep=',')
    return blog
def getTextContent(blog,colName,timeSlice,timeSliceValue):
    #this function is for getting content from dataframe
    import pandas as pd
    content=[]
    #set(blog.timeSlice)
    for l in list(blog[colName][blog[timeSlice]==timeSliceValue].values):
        content.append(l.decode('utf-8'))
    return content
# the following funcs are for data type convert
def fromtuple2list(contenttuple):
    #this is for convert tuple to list
    contentlist=[]
    for c in contenttuple:
        contentlist.append(c[0])
    return contentlist
def listlist2list(contenttext):
    # this is for nested list to list
    contentlist=[]
    for con in contenttext:
        for c in con:
            if c.isalpha():
                contentlist.append(c) 
    return contentlist
def getconentfrommysql(commond):
    from mysqldb import Mysqldb
    #this is for connect mysql to get blog content
    mysqldb_try=Mysqldb()
    mysqldb_try.mysqldb()
    count = mysqldb_try.cur.execute(commond)
    content=mysqldb_try.cur.fetchmany(count)
    mysqldb_try.con.commit()
    mysqldb_try.cur.close()
    return content
def getFileName(raw_dict_motherpath):
    #input is the motherpath
    import os 
    FileList=[] 
    FileName=[]
    FileNames=os.listdir(raw_dict_motherpath) 
    if (len(FileNames)>0): 
        for fn in FileNames: 
            if (len('')>0): 
                 #返回指定类型的文件名 
                if (IsSubString(FlagStr,fn)): 
                    fullfilename=os.path.join(raw_dict_motherpath,fn) 
                    FileList.append(fullfilename)
                    FileName.append(fn[:-4]) 
            else: 
                #默认直接返回所有文件名 
                fullfilename=os.path.join(raw_dict_motherpath,fn) 
                FileList.append(fullfilename) 
                FileName.append(fn[:-4]) 
    #对文件名排序 
    #if (len(FileList)>0): 
    #    FileList.sort() 
    FileList_FileName=zip(FileList,FileName)
    return FileList_FileName
def ischinese(word):
    import re
    pattern = re.compile(u"[\u4e00-\u9fa5]{1,2}")
    if pattern.findall(word):
        return True
    else:
        return False 
