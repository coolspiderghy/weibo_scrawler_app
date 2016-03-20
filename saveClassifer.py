#-*-coding=utf8-*-
import sklearn
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

import evalueClassier as ec
import extractFeatures as ef
import evalueClassier as ec
#把分类器存储下来
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
#Train and save classifier
NuSVC_classifier = SklearnClassifier(NuSVC(probability=True))
NuSVC_classifier.train(trainSet)
pickle.dump(NuSVC_classifier, open('/Users/genghaiyang/ghy_works/projects/weibo_crawler/textmining/sentiML/NuSVC_classifier.pkl','w'))