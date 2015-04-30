#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''
import os
import urllib 
import urllib2
import cookielib
#python瀛楃涓蹭互鍙婃枃浠跺鐞�http://www.jb51.net/article/47956.htm锛沨

#杩斿洖鎸囧畾閰嶇疆鏂囦欢鐨勫湴鍧�
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
    #璇诲彇url鍜屽搴斿弬鏁板苟瀛樺偍鍦ㄥ瓧鍏镐腑
    url_param={}
    s="label"
    e="]"
    for line in file_object:
        m=line.find(s)
        n=line.find(e)
        if (m>0):
            url=line[m+8:n-1]
            param=line[n+6:-3]
            url_param[url]=param
    for item in url_param.items():print item

if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words