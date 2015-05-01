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

def post(url, data):  
    #http post方法
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
    #获得param_list中元素的值，存储在字典中并返回
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
            if(p.find("&")<0):#最后一个参数
                e1=p.find("=")
                s1=0
                name=p[s1:e1]
                value=p[e1+1:]
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
            #param=re.findall(r'\'([^\']*)\'([^\']*)$', line)
            p = re.compile(r'\'([^\']*)\'([^\']*)$')
            tem_para=""
            for m in p.finditer(line):
                tem_para=m.group()
            p = re.compile(r'(?<=\').*(?=\')')
            for m in p.finditer(tem_para):
                param = m.group()     
        if (param.__str__().find('=')>0):
            url_list.append(url)
            param_list.append(param)
        else:
            if(url<>""):
                url_list.append(url)
                param_list.append("")
    return url_list,param_list

def auto_visiter():
    data={}  
    get_url_param("addtocart.dot")
    num=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    #按照图文件的顺序访问再访问一遍
    while(len(param_list)>num):
        if(param_list[num]==""):#get
            urllib2.urlopen("http://"+url_list[num].__str__())
        else:#post
            data=get_post_data(param_list[num])
            print post("http://"+url_list[num].__str__(),data)
        num=num+1

if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words