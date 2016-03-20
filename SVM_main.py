#-*-coding:utf-8-*-
"""
第一步，载入数据。
要做情感分析，首要的是要有数据。
数据是人工已经标注好的文本，有一部分积极的文本，一部分是消极的文本。
文本是已经分词去停用词的商品评论，形式大致如下：[[word11, word12, ... word1n], [word21, word22, ... , word2n], ... , [wordn1, wordn2, ... , wordnn]]
这是一个多维数组，每一维是一条评论，每条评论是已经又该评论的分词组成。
pos_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/pos_review.pkl','r'))
neg_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/neg_review.pkl','r'))

#第二步，使积极文本的数量和消极文本的数量一样。

from random import shuffle
shuffle(pos_review) #把积极文本的排列随机化
size = int(len(pos_review)/2 - 18)
pos = pos_review[:size]
neg = neg_review
neg_review = neg_review*3
pos = pos_review[:50]
neg = neg_review[:50]

#计算整个语料里面每个词和双词搭配的信息量
posWords = list(itertools.chain(*posdata))
negWords = list(itertools.chain(*negdata))

bigram_finder = BigramCollocationFinder.from_words(posWords)
bigram_finder = BigramCollocationFinder.from_words(negWords)
posBigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 5000)
negBigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 5000)

pos = posWords + posBigrams #词和双词搭配
neg = negWords + negBigrams
    
create_word_scores(posWords,negWords)
word 
bigram
word+bigram
"""
"""
there are several different kinds of feature selection
1. 使用所有词作为特征
2. 使用双词搭配作特征
3. 使用所有词加上双词搭配作特征
4. 使用信息量丰富的词作为分类特征
5. 使用信息量丰富的词和双词作为分类特征
"""
import evalueClassier as ec
import extractFeatures as ef
import pickle
import itertools 
import evalueClassier as ec
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
# select positive and negative features.
pos_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/pos_review.pkl','r'))
neg_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/neg_review.pkl','r'))
neg_review = neg_review*3
pos = pos_review[:50]
neg = neg_review[:50]

word_scores = ef.create_word_scores(pos,neg,'pos','neg')
best_words = ef.find_best_words(word_scores, 1000)
posFeatures = []
for p in pos:
    pos_selected = ef.best_word_features(p,best_words)
    posFeatures.append(ef.tagFeatures(pos_selected,'pos'))
negFeatures = []
for n in neg:
    neg_selected = ef.best_word_features(n,best_words)
    negFeatures.append(ef.tagFeatures(neg_selected,'neg'))

# divide Features into train devtest and test sets.
trainSet = posFeatures[:50]+negFeatures[:50]
devtestSet = posFeatures[40:50]+negFeatures[40:50]
testSet = posFeatures[40:50]+negFeatures[40:50]
print testSet
classifer_dict={'BernoulliNB':BernoulliNB(),'MultinomialNB':MultinomialNB(),'LogisticRegression':LogisticRegression(),'SVC':SVC(),'LinearSVC':LinearSVC(),'NuSVC':NuSVC()}
for classiferName,classiferFunc in classifer_dict.items():
    ec.showEvalueResult(trainSet,devtestSet,classiferName,classiferFunc)