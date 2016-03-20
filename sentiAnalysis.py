#! /usr/bin/env python2.7
#coding=utf-8
#import sys 
#reload(sys) 
#sys.setdefaultencoding('utf-8')
import pickle
import textprocessing as tp
import numpy as np
"""
GHY,before analysis, there are several stuff needed to do, 
first, sentiment_dictionaries are necessary.
- just use bisic version of HowNet,no
- get all dict
second,textprocessing module is needed to cut text into individual sentence.
- find a solution to cut sentence,yes
"""
def make_dictpkl(raw_dict_motherpath,dicts_path):
    import tp_utility as tpu
    for dict_path,dict_name in tpu.getFileName(raw_dict_motherpath):
        dict=[]
        dictfile = open(dict_path,'r')
        for dict_word in dictfile.readlines():
            dict_word = dict_word.decode('utf-8')
            dict_word = dict_word.replace(' \n','')
            #print dict_word
            if dict_word !='' and tpu.ischinese(dict_word):#or  dict_word >= u'\u4e00' and dict_word<=u'\u9fa5':
                #print dict_word
                dict.append(dict_word)
        pickle.dump(dict, open(dicts_path+'/'+dict_name+'.pkl','wb'))
def load_dictpickle(dict_motherpath):
    import tp_utility as tpu
    dicts = []
    for dict_path,dict_name in tpu.getFileName(dict_motherpath):
        dicts.append(pickle.load(open(dict_path, 'r')))
    global insufficientdict,inversedict,ishdict, moredict,mostdict,negdict,posdict,verydict
    insufficientdict = dicts[0]
    inversedict = dicts[1]
    ishdict = dicts[2]
    moredict = dicts[3]
    mostdict = dicts[4]
    negdict = dicts[5]
    posdict = dicts[6]
    verydict = dicts[7]
def judgeodd(num):
    if (num/2)*2 == num:
        return 'even'
    else:
        return 'odd'
def sentiment_score(senti_score_list):
    score = []
    for senti_score in senti_score_list:
        score_array = np.array(senti_score)
        Pos = np.sum(score_array[:,0])
        Neg = np.sum(score_array[:,1])
        AvgPos = np.mean(score_array[:,0])
        AvgNeg = np.mean(score_array[:,1])
        StdPos = np.std(score_array[:,0])
        StdNeg = np.std(score_array[:,1])
        score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score
def mysentiment_score_list(oneblog):
    cuted_data = []
    for sen in tp.cut_sentence(oneblog):
        cuted_data.append(sen)
    blog_score_list = []
    for sent in cuted_data:  #循环遍历评论中的每一个分句
        segtmp = tp.segmentation(sent)
        #print segtmp
        pos_count = 0
        neg_count = 0
        for word in segtmp:
            if word in posdict:
                pos_count +=1
            elif word in negdict:
                neg_count +=1
        blog_score_list.append([pos_count,neg_count])
    return blog_score_list 
def sentiment_score_list(oneblog):
    cuted_data = []
    for sen in tp.cut_sentence(oneblog):
        #print sen
        cuted_data.append(sen)
    #print 'testing..............'
    count1 = []
    count2 = []
    #for sents in cuted_data: #循环遍历每一个评论
    for sent in cuted_data:  #循环遍历评论中的每一个分句
        segtmp = tp.segmentation(sent)  #把句子进行分词，以列表的形式返回
        #segtmp =list(set(segtmp)) #去除用于的词，如果情感词出现多次，那么会被重复计算
        #print segtmp
        i = 0 #记录扫描到的词的位置
        a = 0 #记录情感词的位置
        poscount = 0 #积极词的第一次分值
        poscount2 = 0 #积极词反转后的分值
        poscount3 = 0 #积极词的最后分值（包括叹号的分值）
        negcount = 0
        negcount2 = 0
        negcount3 = 0
        for word in segtmp:
            #print word,type(word),'testing...........'
            if word in posdict: #判断词语是否是情感词
                poscount += 1                
                c = 0
                for w in segtmp[a:i]:  #扫描情感词前的程度词
                    if w in mostdict:
                        poscount *= 4.0
                    elif w in verydict:
                        poscount *= 3.0
                    elif w in moredict:
                        poscount *= 2.0
                    elif w in ishdict:
                        poscount /= 2.0
                    elif w in insufficientdict:
                        poscount /= 4.0
                    elif w in inversedict:
                        c += 1
                if judgeodd(c) == 'odd': #扫描情感词前的否定词数
                    poscount *= -1.0
                    poscount2 += poscount
                    poscount = 0
                    poscount3 = poscount + poscount2 + poscount3
                    poscount2 = 0
                else:
                    poscount3 = poscount + poscount2 + poscount3
                    poscount = 0
                a = i + 1 #情感词的位置变化
            elif word in negdict: #消极情感的分析，与上面一致
                negcount += 1
                d = 0
                for w in segtmp[a:i]:
                    if w in mostdict:
                        negcount *= 4.0
                    elif w in verydict:
                        negcount *= 3.0
                    elif w in moredict:
                        negcount *= 2.0
                    elif w in ishdict:
                        negcount /= 2.0
                    elif w in insufficientdict:
                        negcount /= 4.0
                    elif w in inversedict:
                        d += 1
                if judgeodd(d) == 'odd':
                    negcount *= -1.0
                    negcount2 += negcount
                    negcount = 0
                    negcount3 = negcount + negcount2 + negcount3
                    negcount2 = 0
                else:
                    negcount3 = negcount + negcount2 + negcount3
                    negcount = 0
                a = i + 1
            elif word == '！'.decode('utf8') or word == '!'.decode('utf8'): ##判断句子是否有感叹号
                for w2 in segtmp[::-1]: #扫描感叹号前的情感词，发现后权值+2，然后退出循环
                    if w2 in posdict or negdict:
                        poscount3 += 2
                        negcount3 += 2
                        break                    
            i += 1 #扫描词位置前移

        #print pos_count,neg_count,'testing...................'
    #以下是防止出现负数的情况
        pos_count = 0
        neg_count = 0
        if poscount3 < 0 and negcount3 > 0:
            neg_count += negcount3 - poscount3
            pos_count = 0
        elif negcount3 < 0 and poscount3 > 0:
            pos_count = poscount3 - negcount3
            neg_count = 0
        elif poscount3 < 0 and negcount3 < 0:
            neg_count = -poscount3
            pos_count = -negcount3
        else:
            pos_count = poscount3
            neg_count = negcount3
            
        count1.append([pos_count, neg_count])
    count2.append(count1)
    count1 = []    
    return count2
def sentiAnalysis_snownlp(contentlist): 
    #情感分析
    from snownlp import SnowNLP
    senti=[(SnowNLP(i).sentiments,i) for i in contentlist] 
    return senti