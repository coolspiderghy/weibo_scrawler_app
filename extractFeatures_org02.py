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
def create_word_scores(posWords,negWords):
    # import all yuliao
    import itertools 
    from nltk.probability import FreqDist, ConditionalFreqDist 
    def count_fd(valueWords,tag):   
        Words = list(itertools.chain(*valueWords)) #把多维数组解链成一维数组
        word_fd = FreqDist() #可统计所有词的词频
        cond_word_fd = ConditionalFreqDist() #可统计积极文本中的词频和消极文本中的词频
        for word in Words:
            word_fd[word] += 1#word_fd.inc(word)
            cond_word_fd[tag][word]+= 1#cond_word_fd['pos'].inc(word)        
        word_count = cond_word_fd[tag].N() #词数量
        return word_fd,cond_word_fd,tag,word_count
    """
    def count_fd(valueWords,tag):    
        Words[0] = list(itertools.chain(*valueWords)) #把多维数组解链成一维数组
        word_fd = FreqDist() #可统计所有词的词频
        cond_word_fd = ConditionalFreqDist() #可统计积极文本中的词频和消极文本中的词频
        for word in Words[0]:
            word_fd[word] += 1#word_fd.inc(word)
            cond_word_fd[tag[0]][word]+= 1#cond_word_fd['pos'].inc(word)
        for word in Words[1]:
            word_fd[word] += 1#word_fd.inc(word)
            cond_word_fd[tag[1]][word]+= 1#cond_word_fd['pos'].inc(word)            
        word_count[0] = cond_word_fd[tag[0]].N() #词数量
        word_count[1] = cond_word_fd[tag[1]].N() #词数量
        return word_fd,cond_word_fd,tag,word_count[0],word_count[1]
    """
    total_word_count = count_fd(posWords,'pos')[3]+count_fd(negWords,'neg')[3]
    # get words_scores
    def all_word_scores(total_word_count,*args):#word_fd,cond_word_fd,tag,word_count):  
        #print args#count_fd(posWords,'pos')[0]
        word_fd,cond_word_fd,tag,word_count=args[0][0],args[0][1],args[0][2],args[0][3]
        #print word_fd,cond_word_fd,tag,word_count
        word_score = []
        for word, freq in word_fd.iteritems():
            score = BigramAssocMeasures.chi_sq(cond_word_fd[tag][word], (freq, word_count), total_word_count) #计算积极词的卡方统计量，这里也可以计算互信息等其它统计量
            word_score.append((word,score))
        return word_score
    word_scores={}
    for word_score in all_word_scores(total_word_count,count_fd(posWords,'pos')):
        word_scores.setdefault(word_score[0],word_score[1])
    for word_score in all_word_scores(total_word_count,count_fd(posWords,'neg')):
        word_scores.setdefault(word_score[0],word_score[1]) 
    return word_scores #包括了每个词和这个词的信息量    
    #word_scores[word] = pos_score + neg_score #一个词的信息量等于积极卡方统计量加上消极卡方统计量
#根据信息量进行倒序排序，选择排名靠前的信息量的词
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