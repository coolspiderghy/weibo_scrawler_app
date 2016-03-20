#-*-coding=utf-8-*-
import mystats
from Count import *
from pandas import *
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
#from nlp import pre_process_cn
def makeBlogFamework(path,filename):
    mystats.extendTime(path,filename)
    newfile = path+'/new_'+filename+'.csv'
    blog = read_csv(newfile, header='infer', sep=',')
    return blog
# this block for plot time-freq histgram for individuals
def plot_hist(runornot):
    while runornot:
        plt.figure(1)
        timelist = ['year','month','day','hour','dayofweek']
        layoutlist = [231,232,234,235,236]
        for timeiterm in timelist:
            plt.subplot(layoutlist[timelist.index(timeiterm)])
            plt.hist(blog[timeiterm].values, bins = len(set(blog[timeiterm].values)), facecolor='blue', alpha=0.5)
            #plt.xlabel()
            plt.ylabel('freq')
            plt.title(timeiterm)
            #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
            #plt.axis([40, 160, 0, 0.03])
            #plt.grid(True)
        plt.show()
        #.title('Histogram')
        plt.show()
path  = './data/data10'
filename = 'smallS' 
blog=makeBlogFamework(path, filename)
plot_hist(False)
'''
wordlist=[]
for c in contenttext:
    for i in c:
        wordlist.append(i.encode('utf-8'))
'''
   
# I plan to do text mining, 1. word freq, 2. affective analysis, in the framework of time, affective change 3. ML 4.; 
"""
what I need to do?
make it clear: conception? package or modules to do that work, what main logic in this analysis?
what are main steps of natural language process?
词性标注、名词短语抽取、情感分析、分类、翻译
词性标注、名词短语抽取、情感分析、分类、翻译
词性标注工具(Part-Of-Speech Tagger)，N元搜索(n-gram search)，情感分析(sentiment analysis)，WordNet
Polyglot,136种语言的情感分析
"""