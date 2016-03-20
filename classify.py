#-*-coding=utf8-*-
import pandas as pd
def get_best_words():
    import extractFeatures as ef
    import pickle
    pos_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/pos_review.pkl','r'))
    neg_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/neg_review.pkl','r'))
    neg_review = neg_review*3
    pos = pos_review[:50]
    neg = neg_review[:50]
    word_scores = ef.create_word_scores(pos,neg,'pos','neg')
    best_words = ef.find_best_words(word_scores, 10000)
    return best_words

def extract_features(data):
    import extractFeatures as ef
    best_words = get_best_words()
    feat = []
    for i in data:
        feat.append(ef.best_word_features(i,best_words))
    return feat
def get_blog_features():
    import tp_utility as tpu
    import textprocessing as tp
    import MySQLdb
    #get blog df_content
    mysql_cn= MySQLdb.connect('127.0.0.1','root','100811','mydb',charset='utf8')
    df_content = pd.read_sql("select * from weibo_bloginfor limit 5000;", con=mysql_cn)    
    mysql_cn.close()
    #get features in each blog
    blogs= df_content['mc'].values
    moto =  [tp.segmentation(blog) for blog in blogs]
    moto_features = extract_features(moto)
    return moto_features,df_content
def get_tablewithsentiprob():
    import pickle
    import sklearn
    #load classifier
    moto_features,df_content = get_blog_features()
    clf = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/NuSVC_classifier.pkl','r'))
    # compute and add senti prob to df_content
    pred = clf.prob_classify_many(moto_features)
    pos_pro_list = []
    neg_pro_list = []
    for i in pred:
        pos_pro_list.append(i.prob('pos'))
        neg_pro_list.append(i.prob('neg'))
    df_content['pos_pro']=pos_pro_list
    df_content['neg_pro']=neg_pro_list
    df_content[['pos_pro','neg_pro']]
    return df_content
def save_mysql():
    # save df_content with senti probability into mysql mydb
    import MySQLdb
    mysql_cn= MySQLdb.connect('127.0.0.1','root','100811','mydb',charset='utf8')
    df_contentwithsentiprob = get_tablewithsentiprob()
    df_contentwithsentiprob.index=df_contentwithsentiprob['pt'].values
    df_contentwithsentiprob.to_sql(con=mysql_cn, name='weibo_bloginfor4senti', if_exists='replace', flavor='mysql')
    mysql_cn.close()
import MySQLdb
#get blog df_content
mysql_cn= MySQLdb.connect('127.0.0.1','root','100811','mydb',charset='utf8')
df_content = pd.read_sql("select * from weibo_bloginfor4senti where un='_-Crrrr'limit 500;", con=mysql_cn)    
mysql_cn.close()
df_content.index=df_content['pt']
df_content_pos_neg_pro=df_content.loc[:,['pos_pro']]
#df_content_pos_neg_pro.cumsum()
import matplotlib.pyplot as plt
#plt.figure()
df_content_pos_neg_pro.plot()
plt.show()