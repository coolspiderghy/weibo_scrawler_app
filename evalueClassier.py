#-*-coding=utf8-*-
import sklearn
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def buildClassifier_score(trainSet,devtestSet,classifier):
    #print devtestSet
    from nltk import compat
    dev, tag_dev = zip(*devtestSet) #把开发测试集（已经经过特征化和赋予标签了）分为数据和标签
    classifier = SklearnClassifier(classifier) #在nltk 中使用scikit-learn 的接口
    #x,y in  list(compat.izip(*trainSet))
    classifier.train(trainSet) #训练分类器
    #help('SklearnClassifier.batch_classify')
    pred = classifier.classify_many(dev)#batch_classify(testSet) #对开发测试集的数据进行分类，给出预测的标签
    return accuracy_score(tag_dev, pred) #对比分类预测结果和人工标注的正确结果，给出分类器准确度
def showEvalueResult(trainSet,devtestSet,classiferName,classiferFunc):
    print classiferName +'`s accuracy is %f' %buildClassifier_score(trainSet,devtestSet,classiferFunc)
"""
BernoulliNB()
MultinomialNB()
LogisticRegression()
SVC()
LinearSVC()
NuSVC()
"""