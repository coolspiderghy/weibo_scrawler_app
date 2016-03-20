# -*- coding: utf-8 -*- 
content =((u'\u5fc3\u8840\u6765\u6f6e\u60f3\u51fa\u4e2aHani\u4eff\u5986\u2026\u5316\u4e86\u4e00\u4e2a\u773c\u775b\u600e\u4e48\u90fd\u4e0d\u50cf',), (u'\u6211\u5ba4\u53cb\u559c\u6b22\u9ec4\u5b50\u97ec@CHENshu-',))
def fromtuple2list(contenttuple):
    contentlist=[]
    for c in contenttuple:
        contentlist.append(c[0])
    return contentlist
print fromtuple2list(content)

# I guess this is all about headers and cookie