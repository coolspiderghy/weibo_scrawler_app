#-*-coding=utf-8-*-
def count(seq):
    if type(seq)==list:
        tmplist=seq
    else:
        tmplist = list(seq)
    count = len(seq)
    myset = set(tmplist)
    x=list()
    cnt=0
    for item in myset:
        #if is_chinese(item):
        #    item=item.encode('utf-8')
        x.append((item,100*tmplist.count(item)/count))
    return x
def is_chinese(uchar):

        """判断一个unicode是否是汉字"""

        if uchar >= u'/u4e00' and uchar<=u'/u9fa5':

                return True

        else:

                return False