#-*-coding=utf8-*-
import sklearn
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import Tagging
from Tagging import *
"""
#一、使用测试集测试分类器的最终效果
#word_scores = create_word_bigram_scores() #使用词和双词搭配作为特征
#best_words = find_best_words(word_scores, 1500) #特征维度1500

posFeatures = pos_features(best_word_features)
negFeatures = neg_features(best_word_features)

#trainSet = posFeatures[:500] + negFeatures[:500] #使用了更多数据
#testSet = posFeatures[500:] + negFeatures[500:]

train = posFeatures[:25]+negFeatures[:25]
testSet = posFeatures[25:35]+negFeatures[25:35]
test = posFeatures[35:50]+negFeatures[35:50]

test, tag_test = zip(*testSet)

def final_score(classifier):
    classifier = SklearnClassifier(classifier)
    classifier.train(trainSet)
    pred = classifier.batch_classify(test)
    return accuracy_score(tag_test, pred)

print final_score(NuSVC())#BernoulliNB()) #使用开发集中得出的最佳分类器
"""
#二、把分类器存储下来
#（存储分类器和前面没有区别，只是使用了更多的训练数据以便分类器更为准确）
word_scores = create_word_bigram_scores()
best_words = find_best_words(word_scores, 1500)

posFeatures = pos_features(best_word_features)
negFeatures = neg_features(best_word_features)

#trainSet = posFeatures + negFeatures
trainSet = posFeatures[:25]+negFeatures[:25]
testSet = posFeatures[25:35]+negFeatures[25:35]
test = posFeatures[35:50]+negFeatures[35:50]

NuSVC_classifier = SklearnClassifier(NuSVC(probability=True))
NuSVC_classifier.train(trainSet)
pickle.dump(NuSVC_classifier, open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/NuSVC_classifier.pkl','w'))

#在存储了分类器之后，就可以使用该分类器来进行分类了。
#三、使用分类器进行分类，并给出概率值
#给出概率值的意思是用分类器判断一条评论文本的积极概率和消极概率。给出类别也是可以的，也就是可以直接用分类器判断一条评论文本是积极的还是消极的，但概率可以提供更多的参考信息，对以后判断评论的效用也是比单纯给出类别更有帮助。

#1. 把文本变为特征表示的形式
#要对文本进行分类，首先要把文本变成特征表示的形式。而且要选择和分类器一样的特征提取方法。
#moto = pickle.load(open('D:/code/review_set/senti_review_pkl/moto_senti_seg.pkl','r')) #载入文本数据
#moto = test
def extract_features(data):
    feat = []
    for i in data:
        feat.append(best_word_features(i))
    return feat

moto_features, tag_test = zip(*test)
#moto_features = extract_features(moto) #把文本转化为特征表示的形式
#注：载入的文本数据已经经过分词和去停用词处理。

#2. 对文本进行分类，给出概率值
import pickle
import sklearn

clf = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/NuSVC_classifier.pkl','r')) #载入分类器

pred = clf.prob_classify_many(moto_features)#batch_prob_classify(moto_features) #该方法是计算分类概率值的
p_file = open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/test_results/results.txt','w') #把结果写入文档
for i in pred:
    p_file.write(str(i.prob('pos')) + ' ' + str(i.prob('neg')) + '\n')
p_file.close()