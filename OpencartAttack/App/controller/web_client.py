#coding:utf-8
'''
Created on 2015��5��25��

@author: Administrator

'''
#�µ����滻auto_visitor����̫�෽����Ҫ���������½���
import os
import urllib 
import urllib2
import cookielib
import re
from data import url_list
from data import param_list
from cookielib import Cookie
import thread 

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

def test_session():
    
    def session1():
        print 'session1'
        get_url_param("G://Graph4.dot")
        num=0
        cj = cookielib.CookieJar();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
        urllib2.install_opener(opener);
        while(len(param_list)>num):
            if(param_list[num]==""):#get
                print url_list[num].__str__()
                get(url_list[num].__str__(),opener)
            else:#post
                print 'url is ',url_list[num].__str__()                
                get_post_data(param_list[num])
            num=num+1
        cook=cj._cookies
        print 'session1 end'
        #thread.exit_thread()  
        print 'session1 end2'
        return cook.get('211.87.234.178').get('/').get('PHPSESSID')
    
    def session2(session):
        print 'session2'
        get_url_param("G://Graph4.dot")
        num=0
        cj = cookielib.CookieJar();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
        urllib2.install_opener(opener);
        urllib2.urlopen("http://211.87.234.178")
    
        cook=cj._cookies
    #cookie structure ([domain[, path[, name]]])
        cook.get('211.87.234.178').get('/').get('PHPSESSID').value=session
        print 'session2 cook',cook
        while(len(param_list)>num):
            if(param_list[num]==""):#get
                print url_list[num].__str__()
                get(url_list[num].__str__(),opener)
            else:#post
                print 'url is ',url_list[num].__str__()                
                get_post_data(param_list[num])
    
            num=num+1
        print 'session2 end'
        #thread.exit_thread()  
        #return cook.get('211.87.234.178').get('/').get('PHPSESSID')
        
    thread1=session1()
    print 'between'
    thread2=session2('s')
    print 'alalalalaalalalalalaalalalalalalalalalalalalalalalal'
    #thread.start_new_thread(session1(),(1,1)).jion


def auto_visiter():
    data={}  
    get_url_param("G://Graph4.dot")
    num=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    response=urllib2.urlopen("http://211.87.234.178")
    
    cook=cj._cookies
    #cookie structure ([domain[, path[, name]]])
    cook.get('211.87.234.178').get('/').get('PHPSESSID')
    print  cook.get('211.87.234.178').get('/').get('PHPSESSID').value

    #a=cookielib(s)
   # print a

    
    #{'/': {'PHPSESSID': Cookie(version=0, name='PHPSESSID', value='5lr7heudd9r3o4b1af3spjsv93', port=None, port_specified=False, domain='211.87.234.178', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)}}

    print 'cook',cook
  
    
    test_string="string"
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
