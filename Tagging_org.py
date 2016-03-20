#coding=utf-8
from extractFeatures import *
import pickle
"""
第一步，载入数据。
要做情感分析，首要的是要有数据。
数据是人工已经标注好的文本，有一部分积极的文本，一部分是消极的文本。
文本是已经分词去停用词的商品评论，形式大致如下：[[word11, word12, ... word1n], [word21, word22, ... , word2n], ... , [wordn1, wordn2, ... , wordnn]]
这是一个多维数组，每一维是一条评论，每条评论是已经又该评论的分词组成。
"""
pos_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/pos_review.pkl','r'))
neg_review = pickle.load(open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/pos_neg_review/neg_review.pkl','r'))
#我用pickle 存储了相应的数据，这里直接载入即可。

#第二步，使积极文本的数量和消极文本的数量一样。
"""
from random import shuffle
shuffle(pos_review) #把积极文本的排列随机化
size = int(len(pos_review)/2 - 18)
pos = pos_review[:size]
neg = neg_review
"""
neg_review = neg_review*3
pos = pos_review[:50]
neg = neg_review[:50]
#我这里积极文本的数据恰好是消极文本的2倍还多18个，所以为了平衡两者数量才这样做。

#第三步，赋予类标签。
def pos_features(feature_extraction_method):
    posFeatures = []
    for i in pos:
        posWords = [feature_extraction_method(i),'pos'] #为积极文本赋予"pos"
        posFeatures.append(posWords)
    return posFeatures

def neg_features(feature_extraction_method):
    negFeatures = []
    for j in neg:
        negWords = [feature_extraction_method(j),'neg'] #为消极文本赋予"neg"
        negFeatures.append(negWords)
    return negFeatures
#这个需要用特征选择方法把文本特征化之后再赋予类标签。
#第四步、把特征化之后的数据数据分割为开发集和测试集
#这里把前124个数据作为测试集，中间50个数据作为开发测试集，最后剩下的大部分数据作为训练集。