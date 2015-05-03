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
url_list=[]
param_list=[]

def get(url,opener):
    resp = opener.open("http://"+url);   
    return resp

def post(url, data,opener):  
    url="https://"+url
    data = urllib.urlencode(data)  
    req=urllib2.Request(url,data)
    response = opener.open(req)  
    return response

def getconfigRoute():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]+"\conf\config.txt"
    return route

def get_post_data(param_list_element):
    #获得param_list中元素的值，存储在字典中并返回
    p=param_list_element
    data={}
    while(len(p)>1):
        s=0
        e=p.find("^_^")
        if(e>0):
            tem=p[s:e]
            s=e+3
            p=p[s:]
            e1=tem.find("$_$")
            s1=0
            name=tem[s1:e1]
            value=tem[e1+3:]
            data[name]=value      
        else:
            break
    return data

def get_url_param(path):
    #正则处理url和param并分别存储在两个list中
    file_object = open(path)
    for line in file_object:
        #line是整个http请求的所有内容
        url=param=""
        if(re.findall(r'label=\".*\"]',line).__str__()<>'[]'):
            #url是中括号内的内容
            p = re.compile(r'(?<=label=\"\s).*(?=\"])')
            for m in p.finditer(line):
                url=m.group()
            url=url.replace('\\r','')
            p = re.compile(r'(?<=//).*')
            for m in p.finditer(line):
                param = m.group()
        if (param.__str__().find('$_$')>0):
            url_list.append(url)
            param_list.append(param)
        else:
            if(url<>""):
                url_list.append(url)
                param_list.append("")
    return url_list,param_list

def auto_visiter():
    data={}  
    get_url_param("Graph3.dot")
    num=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    response=urllib2.urlopen("http://211.87.234.178")
    cook=cj._cookies
    print "cook",cook
    test_string="asdf"
    #按照图文件的顺序访问再访问一遍
    while(len(param_list)>num):
        if(param_list[num]==""):#get
            response=get(url_list[num].__str__(),opener)
            print "get_url",url_list[num]
            if response.__class__==test_string.__class__:
                print response
            else:
                print response.read()
        else:#post
            data=get_post_data(param_list[num])
            print "data",data
            print "post_url",url_list[num]
            response=post(url_list[num].__str__(),data,opener)

            if response.__class__==test_string.__class__:
                print response
            else:
                print response.read()
        num=num+1

def unquote_URL(path):
    return urllib.unquote(path)

if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words
