#-*-coding=utf-8-*-
import pickle
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
# get bag of word
def bag_of_words(words):
    return dict([(word, True) for word in words])
def bigram(words, score_fn=BigramAssocMeasures.chi_sq, n=1000):
    bigram_finder = BigramCollocationFinder.from_words(words)  #把文本变成双词搭配的形式
    bigrams = bigram_finder.nbest(score_fn, n) #使用了卡方统计的方法，选择排名前1000的双词
    return bigrams
#计算整个语料里面每个词的信息量
def create_word_scores(posWords,negWords,posTag,negTag):
    from nltk.probability import FreqDist, ConditionalFreqDist
    import itertools 
    posWords = list(itertools.chain(*posWords)) #把多维数组解链成一维数组
    negWords = list(itertools.chain(*negWords)) #同理

    word_fd = FreqDist() #可统计所有词的词频
    cond_word_fd = ConditionalFreqDist() #可统计积极文本中的词频和消极文本中的词频
    for word in posWords:
        #help(FreqDist)
        word_fd[word] += 1#word_fd.inc(word)
        cond_word_fd[posTag][word]+= 1#cond_word_fd['pos'].inc(word)
    for word in negWords:
        word_fd[word] += 1#word_fd.inc(word)
        cond_word_fd[negTag][word]+= 1#cond_word_fd['neg'].inc(word)

    pos_word_count = cond_word_fd[posTag].N() #积极词的数量
    neg_word_count = cond_word_fd[negTag].N() #消极词的数量
    total_word_count = pos_word_count + neg_word_count

    word_scores = {}
    for word, freq in word_fd.iteritems():
        pos_score = BigramAssocMeasures.chi_sq(cond_word_fd[posTag][word], (freq, pos_word_count), total_word_count) #计算积极词的卡方统计量，这里也可以计算互信息等其它统计量
        neg_score = BigramAssocMeasures.chi_sq(cond_word_fd[negTag][word], (freq, neg_word_count), total_word_count) #同理
        word_scores[word] = pos_score + neg_score #一个词的信息量等于积极卡方统计量加上消极卡方统计量

    return word_scores #包括了每个词和这个词的信息量
def find_best_words(word_scores, number):
    best_vals = sorted(word_scores.iteritems(), key=lambda (w,s):s, reverse=True)[:number] #把词按信息量倒序排序。number是特征的维度，是可以不断调整直至最优的
    best_words = set([w for w, s in best_vals])
    #for w,s in best_vals:
    #    print w,'\n'
    return best_words
def best_word_features(features,best_words):
    return dict([(f, True) for f in features if f in best_words])
def tagFeatures(features,tag):
    taggedFeatures = [features,tag]
    return taggedFeatures