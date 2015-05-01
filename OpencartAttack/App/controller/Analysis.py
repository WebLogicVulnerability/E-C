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

def get_post_data(param_list_element):
    p=param_list_element
    data={}
    while(len(p)>1):
        s=0
        e=p.find("&")
        if(e>0):
            tem=p[s:e]
            s=e+1
            p=p[s:]
            e1=tem.find("=")
            s1=0
            name=tem[s1:e1]
            value=tem[e1+1:]
            data[name]=value
        else:
            break
    return data

def add_to_cast(): 
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    urllib2.urlopen("http://211.87.234.178"); 
    urllib2.urlopen("211.87.234.178/index.php?route=product/product&product_id=43")
    data = {'quantity':'1', 'product_id':'43'}
    post("http://211.87.234.178/index.php?route=checkout/cart/add",data)
    
    
def get_url_param(path):
    #正则处理url和param并分别存储在两个list中
    file_object = open(path)
    url_list=[]
    param_list=[]
    for line in file_object:
        url=param=""
        if(re.findall(r'label=\".*\"]',line).__str__()<>'[]'):
            url=re.findall(r'label=\".*\"]',line).__str__()[10:-4]
            url=url.replace('\\r','')
        param=re.findall(r'\'([^\']*)\'([^\']*)$', line)
        if (param.__str__().find('=')>0) :
            param=param.__str__()[3:-13]
            url_list.append(url)
            param_list.append(param)
        else:
            if(url<>""):
                url_list.append(url)
                param_list.append("")
    return url_list,param_list

if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words