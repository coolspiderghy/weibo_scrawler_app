#-*-coding=utf-8-*-
import tp_utility as tpu
import sentiAnalysis as sa
commond = "select mc from weibo_bloginfor where un='_-Crrrr' limit 100,200;"
content = tpu.getconentfrommysql(commond)  
content = tpu.fromtuple2list(content)
#content can also be stored in a pkl.
#content = pickle.load(open('D:/code/review_set/review_pkl/Motorala.pkl', 'r'))
#content = [u'我是一个爱戴的人啊！褒奖！亲爱的！']
raw_dict_path = '/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/materials/dict/dict_raw_utf8'
dict_motherpath = '/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/materials/dict/dicts'
#sa.make_dictpkl(raw_dict_path,dict_motherpath)
sa.load_dictpickle(dict_motherpath)
for c in content:
    print c,sa.sentiment_score(sa.sentiment_score_list(c))
