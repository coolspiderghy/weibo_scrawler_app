from downloader import Downloader 
from accountlib import AccountManager  
import urllib2     
#cookie = "SINAGLOBAL  =  1791602201041.3557.1455610750935 ;ULV  = 1455611177148:2:2:2:7716728692915.958.1455611177145:1455610750940  ;SUBP  =  0033WrSXqPxfM725Ws9jqgMF55529P9D9WWNbPECqqxh2rppyWaDQBvZ5JpX5KMt  ;SUHB  =  0jBJqq9P-KpPgN  ;un = guanglingsan1988@sina.com ;wvr  = 6    ;SUS  =  SID-1340714021-1455611173-GZ-b2ey8-468e97b8ca4455bc4ba3beddabec7cd6  ;SUE   = es%3D8484201c133ec33b03f1ed14aa4534fa%26ev%3Dv1%26es2%3D33ba64a44d9ac86cf555cf05bc397327%26rs0%3DM3QtGCbcUToEqKLA6eAZVpMrEX7u4bQVwvi5fHwr4DhrFNaB0594dwFDsL2CZMg5fRLrIkFt3zc9Bx10kzDewhd7AbovJSdm8cKV0c4V1VEfND1YM3XwCaiwZgbhwWc6jXLCbykNpryMLWTdianTFmPUmFrF0%252BazZmYEFLfT7ww%253D%26rv%3D0   ;SUP   = cv%3D1%26bt%3D1455611174%26et%3D1455697574%26d%3Dc909%26i%3D7cd6%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1340714021%26name%3Dguanglingsan1988%2540sina.com%26nick%3Dschumacher%26fmp%3D%26lcp%3D2012-02-02%252019%253A20%253A09    ;SUB   =  _2A257xq12DeRxGedN71IW8SrMyT2IHXVYtZm-rDV8PUNbvtBeLRnGkW9LHet86m9AJ9R6RMhU07ClXHxqCx1S0A..   ;ALF    = 1487147173   ;SSOLoginState   = 1455611174   ;_s_tentry    = login.sina.com.cn   ;UOR   = ,,login.sina.com.cn    ;Apache   =  7716728692915.958.1455611177145 "  
cookie="SINAGLOBAL=3670791019162.063.1432519568807; ULV=1434184446636:3:1:1:9776813265987.371.1434184446576:1432539758675; SUHB=0S7S3YyGl7ABmk; YF-Ugrow-G0=169004153682ef91866609488943c77f; SUS=SID-5513307770-1434867321-GZ-fdui1-417cce02c02cba62afb4b09ce64141b5; SUE=es%3D77e325518a1eeaab4d42c04535d022d9%26ev%3Dv1%26es2%3Dda7c170b38a64fa4d9b6668f496fa074%26rs0%3DzdWWsJgKtTVoMTjEP3CWSLj5LpFJ5UF0%252BWyN6Q8Sd35saJbSk7N2YdacjGPXamqnsYetxrZNNIwMVsz0JNGf%252FkJZ%252FIv1Bh9YQHxwFkUE3K1i7kZDBboUO0yOR%252Fz0Ucw37WwoeeAGM28l5q%252FSbHFjWwe%252F3DJSj1ZdRE59Qrdrt%252Fo%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1434867321%26et%3D1434953721%26d%3Dc909%26i%3D41b5%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D17%26st%3D0%26uid%3D5513307770%26name%3Dmkqtx11141ua%2540163.com%26nick%3D%25E6%25AF%2581%25E9%25A6%2599%25E5%258A%2588%25E5%25BC%25B9%26fmp%3D%26lcp%3D2015-03-20%252000%253A59%253A43; YF-V5-G0=d22a701aae075ca04c11f0ef68835839; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=9776813265987.371.1434184446576; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; WBStore=0d3077cd0cad2262|undefined; SUB=_2A254giYpDeTxGeNL6lES8CnLzDyIHXVb9hDhrDV8PUJbvNBeLRjHkW8xuQX_wA9ncQZsaP1yWBfuXyq9-w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5iPVj051o7KP9Hly_f8Jud5JpX5K-t; ALF=1466403316; SSOLoginState=1434867321; wvr=6"
     
url='http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=3855095853042261&max_id=3856157879315930&page=1'
'''manager = AccountManager()
manager.init()
manager.login()
'''
'''headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.65 Safari/537.36',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Connection": "keep-alive",
        "Host": "weibo.com"
        }
req = urllib2.Request(url, headers=headers)
#print req,headers
result = urllib2.urlopen(req, timeout=10)
text = result.read()
print text'''
manager = AccountManager()
manager.init()
manager.login()
downloader = Downloader(cookie)
html_data = downloader.download(url)
#print html_data