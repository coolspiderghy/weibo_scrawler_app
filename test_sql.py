#-*-coding=utf-8-*-
import tp_utility as tpu
import sentiAnalysis as sa
import textprocessing as tp
import pickle
import pandas as pd
"""
commond = "select mc from weibo_bloginfor where un='_-Crrrr' limit 1000;"
content = tpu.getconentfrommysql(commond)  
content = tpu.fromtuple2list(content)
#print content
blogs= content
#pos_review =  [tp.segmentation(blog) for blog in blogs[0:500]]
#neg_review = [tp.segmentation(blog) for blog in blogs[500:1000]]
"""
#pos_neg_review_path = '/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review'
#pickle.dump(pos_review, open(pos_neg_review_path+'/'+'pos_review'+'.pkl','wb'))
#pickle.dump(neg_review, open(pos_neg_review_path+'/'+'neg_review'+'.pkl','wb'))
#neg_review=pickle.load(open(pos_neg_review_path+'/'+'neg_review'+'.pkl','r')) 
"""
dimension = ['500','1000','1500','2000','2500','3000']
for d in dimension:
    word_scores = create_word_scores_bigram()
    best_words = find_best_words(word_scores, int(d))

    posFeatures = pos_features(best_word_features)
    negFeatures = neg_features(best_word_features)


    train = posFeatures[174:]+negFeatures[174:]
    devtest = posFeatures[124:174]+negFeatures[124:174]
    test = posFeatures[:124]+negFeatures[:124]
    dev, tag_dev = zip(*devtest)

    print 'Feature number %f' %d
    print 'BernoulliNB`s accuracy is %f' %score(BernoulliNB())
    print 'MultinomiaNB`s accuracy is %f' %score(MultinomialNB())
    print 'LogisticRegression`s accuracy is %f' %score(LogisticRegression())
    print 'SVC`s accuracy is %f' %score(SVC())
    print 'LinearSVC`s accuracy is %f' %score(LinearSVC())
    print 'NuSVC`s accuracy is %f' %score(NuSVC())
"""  
file = '/Users/genghaiyang/git/sina_weibo_crawler/data/data10/smallS_pos_neg.csv'
blog = pd.read_csv(file, header='infer', sep=',')
#pos_review =  [tp.segmentation(blog) for blog in blog['mc'][blog.value=='p']]
neg_review =  [tp.segmentation(blog) for blog in blog['mc'][blog.value=='n']]
pos_neg_review_path = '/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_blog'
#pickle.dump(pos_review, open(pos_neg_review_path+'/'+'pos_review'+'.pkl','wb'))
pickle.dump(neg_review, open(pos_neg_review_path+'/'+'neg_review'+'.pkl','wb'))