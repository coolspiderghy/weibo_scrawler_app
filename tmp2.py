# -*- coding: utf-8 -*-
import time
from datetime import datetime,date
a = "2011-09-28 10:00:00"
#中间过程，一般都需要将字符串转化为时间数组
print time.strptime(a,'%Y-%m-%d %H:%M:%S')[0]
#time.struct_time(tm_year=2011, tm_mon=9, tm_mday=27, tm_hour=10, tm_min=50, tm_sec=0, tm_wday=1, tm_yday=270, tm_isdst=-1)
#将"2011-09-28 10:00:00"转化为时间戳
print time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
#1317091800.0
#将时间戳转化为localtime
x = time.localtime(1317091800.0)
print time.strftime('%Y-%m-%d %H:%M:%S',x)
#2011-09-27 10:50:00
# plot the figure based on time, for example 
print datetime.strptime(a, "%Y-%m-%d %H:%M:%S").date().weekday()
dayOfWeek = datetime.now().weekday()
print dayOfWeek

dayOfWeek = datetime.today().weekday()
print dayOfWeek



commond = "select mc from weibo_bloginfor order by rand() limit 100;"
content = tpu.getconentfrommysql(commond) 

columnnames = ('un','uid','iu','mid','mc','srn','run','ruid','rmc','pu','rrc','rcc','rpage','rpt','rc','cc','page','pt')
column_content=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for l in range(18):
    for c in content:
        column_content[l].append(c[l])
#print column_content[2]
dict_content = dict(zip(columnnames,column_content))
df_content = pd.DataFrame(dict_content)
#print df_content['pt']