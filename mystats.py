#-*-coding:utf-8-*-
import csv
from pandas import *
import time
from datetime import datetime,date
#import numpy as np
'''
csvfile = file(filename,'rb')
reader = csv.reader(csvfile)
count  = 0
for r in reader:
    count=count+1
    print count,r   
csvfile.close()
data = {'name':['ghy','jxq'],'salary':[6000,7000]}
blog_home = DataFrame(data)
blog_home['sex']=['male','female']
#del blog_home['sex']
blog_home.iat[1,2]='xxxx'
print blog_home,'\n',blog_home.iat[1,2]#,blog_home.ix[1],'\n',blog_home.dtypes#blog_home['name']#blog_home['salary']
'''
def extendTime(path,filename):
    file = path+'/'+filename+'.csv'
    blog = read_csv(file, header='infer', sep=',')
    blog_time = DataFrame(columns=['year','month','day','hour','dayofweek'])
    for i in range(0,len(blog)):
        l1=list(time.strptime(blog['pt'][i],'%Y-%m-%d %H:%M')[0:4])
        l2=[datetime.strptime(blog['pt'][i],'%Y-%m-%d %H:%M').weekday()]
        l1.extend(l2)
        blog_time.loc[i]=l1
        #print l1
    new_blog = blog
    for i in ['year','month','day','hour','dayofweek']:
        new_blog.loc[:,i] = blog_time.loc[:,i]
    new_blog.to_csv(path+'/new_'+filename+'.csv',index=False,na_rep='NULL')
#plt.hist(blog_time[blog_time.dayofweek==6]['hour'].values)
if __name__=='__main__':
    path  = './data/data10'
    filename = 'coolspider2008'
    extendTime(path,filename)

# operation on blog, divided by time: day divide into 24 hour, week divide into 7 day, month divide into 30 days, year, divide into 365 days. all time divide into different year.
#count(*) where each year, count(*) each day in one week, count (*) each hour in day.
# for each year:1.how many years, what is each one. 2.each year, count