#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''
import os
import urllib 
import urllib2
import cookielib
import re

def post(url, data):  
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return response.read()

def getconfigRoute():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]+"\conf\config.txt"
    return route

def add_to_cast(): 
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    urllib2.urlopen("http://211.87.234.178"); 
    urllib2.urlopen("211.87.234.178/index.php?route=product/product&product_id=43")
    data = {'quantity':'1', 'product_id':'43'}
    post("http://211.87.234.178/index.php?route=checkout/cart/add",data)
    
def geturl_param():
    file_object = open('addtocart.dot')
    #顺序不对
    for line in file_object:
        if (re.findall(r'label=\".*\"]',line).__str__()<>'[]'):
            url=re.findall(r'label=\".*\"]',line).__str__()[10:-4] 
#     url_param={}
#     s="label"
#     e="]"
#     for line in file_object:
#         m=line.find(s)
#         n=line.find(e)
#         if (m>0):
#             url=line[m+8:n-1]
#             param=line[n+6:-3]
#             url_param[url]=param
#     for item in url_param.items():print item

if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words