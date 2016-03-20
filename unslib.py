#-*-coding=utf-8-*-
def len_uns(filename):
    f = open(filename)
    contents=f.readlines()
    len_uns=len(contents)
    f.close()
    return len_uns
def get_uns_uids(filename):
    uns = []
    uids = []
    f = open(filename)
    contents = f.readlines()
    for line in contents:
        uns.append(line.strip('\n').split('\t')[0])
        uids.append(line.strip('\n').split('\t')[1])
    f.close()
    return (uns[800:],uids[800:]) #finsished 30 from 800,
def isInuun(unn):
    filename = 'uun.txt'
    if unn in get_uns(filename):
        return True
    else:
        return False
def remove_repeateduns(filename):
    user_dic = {}
    f = open(filename)
    contents = f.readlines()
    index = 0
    for line in contents:
        #print line.split('\t')[0],line.split('\t')[1]
        user_dic.setdefault(line.strip('\n').split('\t')[0],line.strip('\n').split('\t')[1])
    f.close()
    uns_before=user_dic.keys()
    uns_after=list(set(uns_before))
    uns_after.sort(key=uns_before.index)
def get_urls(uids):
    urls=[]
    for uid in uids:
        urls.append('http://weibo.com/'+str(uid))
    return urls
    #user_dic[uns_after]
    #sorted(user_dic.items(), key=lambda user_dic:user_dic[0])
    #sorted(user_dic.items(), key=lambda user_dic:user_dic[1])   
    #return uns_after
#print get_uns('uuid.txt'),len_uns('uuid.txt')
            