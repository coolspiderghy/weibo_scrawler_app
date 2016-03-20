# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.65 Safari/537.36'
}
''' "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Connection": "keep-alive",
        "Host": "weibo.com"'''
    
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'username':'guanglingsan1988@sina.com',
            'password':'cunzai7412428'
        })
#登录教务系统的URL
loginUrl = 'http://weibo.com/login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata,headers)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
gradeUrl = 'http://account.weibo.com/set/index?topnav=1&wvr=6'
#'http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=3855095853042261&max_id=3856157879315930&page=2'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read().decode('utf-8','ignore')