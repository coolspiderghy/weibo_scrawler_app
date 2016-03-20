#coding=utf-8
from tp_utility import *
def cut_sentence(words):
    #if type(words)=='unicode':
    #    words=words
    #else:
     #   words = words.decode('utf8')
    start = 0
    i = 0
    sents = []

    punt_list = ',.!?:;~，。！？：；～ #@'.decode('utf8')
    for word in words:
        if words.index(word)!=len(words)-1:
            token_index = words.index(word)+1
            token = words[token_index]
            #print token
            if word in punt_list and token not in punt_list: #检查标点符号下一个字符是否还是标点
                sents.append(words[start:i+1])
                start = i+1
                i += 1
            else:
                i += 1
                token = list(words[start:i+2]).pop() # 取下一个字符
    if start < len(words):
        sents.append(words[start:])
    return sents
def segmentation(document):
    """
     简化的 中文+英文 预处理
        1.去掉停用词
        2.去掉标点符号
        3.处理为词干
        4.去掉低频词
 
    """
    import nltk
    import jieba.analyse
    from nltk.tokenize import word_tokenize
    #nltk.download('punkt')
    low_freq_filter = True
    texts_tokenized = []
    #for document in courses:
    #print document
    texts_tokenized_tmp = []
    for word in jieba.cut_for_search(document):#word_tokenize(document):
        texts_tokenized_tmp += jieba.analyse.extract_tags(word,10)
        texts_tokenized.append(texts_tokenized_tmp)   
    
    texts_filtered_stopwords = texts_tokenized
    #print texts_filtered_stopwords
    #去除标点符号
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if not word in english_punctuations] for document in texts_filtered_stopwords]
 
    #词干化
    from nltk.stem.lancaster import LancasterStemmer
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in docment] for docment in texts_filtered]
    
    #去除过低频词
    if low_freq_filter:
        all_stems = sum(texts_stemmed, [])
        stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 0) # this is the threshold of freq of word
        texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
    else:
        texts = texts_stemmed
    #去数字
    return listlist2list(texts)
def getWordFreq(lib_texts):
    from gensim import corpora, models, similarities
    dictionary = corpora.Dictionary(lib_texts)
    corpus = [dictionary.doc2bow(text) for text in lib_texts]
    return corpus