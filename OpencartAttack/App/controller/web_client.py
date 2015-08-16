#-*-coding:utf-8-*
'''
Created on 2015��5��25��

@author: Administrator

'''
#�µ����滻auto_visitor����̫�෽����Ҫ���������½���
import os
import urllib 
import urllib2
import cookielib
import ssl
from data import url_list,url_set,data_set
from data import param_list,cookie
from App.core.parse.parseworkflow import analyze_workflow
from App.core.parse.parseroute import get_config_route,get_current_route
from copy import deepcopy


_error=['error','exception','warning']


def get(url,opener):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheader(headers)
    resp = opener.open("http://"+url);  
    if resp.code.__str__()[0]=='4':
        print 'request error,status code is ',resp.code.__str__()
        exit 
    elif resp.code.__str__()[0]=='5':
        print 'server error,status code is ',resp.code.__str__()
        exit
    return resp

def post(url, data,opener):  
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheader(headers)
    url="https://"+url
    data = urllib.urlencode(data)  
    req=urllib2.Request(url,data)
    response = opener.open(req)
    if response.code.__str__()[0]=='4':
        print 'reqest error,status code is ',response.code.__str__()
        exit
    elif response.code.__str__()[0]=='5':
        print 'server error,status code is ',response.code.__str__()
        exit
    return response


def test_session():
    def session1():
        print 'session1'
        analyze_workflow(get_current_route()+"Graph.dot")
        num=0
        cj = cookielib.CookieJar();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
        urllib2.install_opener(opener);
        while(len(param_list)>num):
            if(param_list[num]==""):#get
                get(url_list[num].__str__(),opener)
            else:#post
                print 'url is ',url_list[num].__str__()                
                get_post_data(param_list[num])
            num=num+1
        cook=cj._cookies
        print 'session1 end'
        #thread.exit_thread()  
        print 'session1 end2'
        return cook.get('211.87.234.16').get('/').get('PHPSESSID')
    
    def session2(session):
        print 'session2'
        analyze_workflow(get_current_route()+"Graph.dot")
        num=0
        cj = cookielib.CookieJar();
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
        urllib2.install_opener(opener);
        urllib2.urlopen("http://211.87.234.16")
    
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
    session1()
        



def auto_visiter():
    data={}  
    analyze_workflow(get_current_route()+"\Graph4.dot")
    num=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    response=urllib2.urlopen("http://211.87.234.178")
#     
#     cook=cj._cookies
#     #cookie structure ([domain[, path[, name]]])
#     cook.get('211.87.234.178').get('/').get('PHPSESSID')
#     print  cook.get('211.87.234.178').get('/').get('PHPSESSID').value
# 
# 
#     
#     #{'/': {'PHPSESSID': Cookie(version=0, name='PHPSESSID', value='5lr7heudd9r3o4b1af3spjsv93', port=None, port_specified=False, domain='211.87.234.178', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)}}
# 
#     print 'cook',cook
#   
#     
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
        
def exe_the_same_workflow():
    #按照图文件的顺序访问再访问一遍
    #解决https打开失败错误
    ssl._create_default_https_context = ssl._create_unverified_context
    data={}  
    num=0
    i=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    response=urllib2.urlopen("https://www.baidu.com")
    test_string="string"
    while(len(param_list)>num):
        if(param_list[num]==""):#get
            #print "get_url",url_list[num]
            response=get(url_list[num].__str__(),opener)
            #print "get_url",url_list[num]
            if response.__class__==test_string.__class__:
                 print response
            else:
                 print response.read()
        else:#post
            data=get_post_data(param_list[num])
#             print "data",data
#             print "post_url",url_list[num]
            response=post(url_list[num].__str__(),data,opener)

            if response.__class__==test_string.__class__:
                print response
            else:
                print response.read()
        num=num+1

def check_the_workflow():
    #按照图文件的顺序访问再访问一遍,尝试寻找其中的错误,记录其中的cookie信息
    ssl._create_default_https_context = ssl._create_unverified_context
    data={}  
    num=0
    i=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    response=urllib2.urlopen("https://www.baidu.com")
    test_string="string"
    while(len(param_list)>num):
        if(param_list[num]==""):#get
            #print "get_url",url_list[num]
            response=get(url_list[num].__str__(),opener)
            #print "get_url",url_list[num]
#             if response.__class__==test_string.__class__:
#                 if check_error(response) == True:
#                     print 'there is an error in wokrflow'
#                     exit
#             else:
#                 if check_error(response.read())==True:
#                     print 'there is an error in wokrflow'
#                     exit
        else:#post
            data=get_post_data(param_list[num])
#             print "data",data
#             print "post_url",url_list[num]
            response=post(url_list[num].__str__(),data,opener)

#             if response.__class__==test_string.__class__:
#                 if check_error(response) == True:
#                     print 'there is an error in wokrflow'
#                     exit
#             else:
#                 if check_error(response.read())==True:
#                     print 'there is an error in wokrflow'
#                     exit
        num=num+1
        cook=cj._cookies
        cookie=cook
        if response.__class__==test_string.__class__:
            print response

        else:
            print response.read()

        
def check_error(html):
    for items in _error:
        if items in html:
            print 'key \'',items,'appeared'
            print html
            os._exit()
    return False


def get_post_data(param_list_element):
    #���param_list��Ԫ�ص�ֵ���洢���ֵ��в�����
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

def get_all_data():
    #extract all the param in the workflow
    all_data={}
    for param in param_list:
        p=deepcopy(param)
        if p:
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
                    all_data[name]=value      
                else:
                    break
    #print all_data
    return all_data        

def test_simple(url_set,data_set):
    #根据输入的url集和数据集进行访问，返回最终页面
    ssl._create_default_https_context = ssl._create_unverified_context
    data={}  
    num=0
    i=0
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    response=urllib2.urlopen("http://211.87.234.16")
    test_string="string"

    while(len(data_set)>num):
        if(data_set[num]==""):         #get
            
            response=get(url_set[num].__str__(),opener)
#             print "get_url",url_list[num]
#             if response.__class__==test_string.__class__:
#                 print response
#             else:
#                 print response.read()
        else:                          #post
            data=get_post_data(data_set[num])
#             print "data",data
#             print "post_url",url_list[num]
            response=post(url_set[num].__str__(),data,opener)

#             if response.__class__==test_string.__class__:
#                 print response
#             else:
#                 print response.read()
        num=num+1
    if response.__class__==test_string.__class__:
        return response
    else:
        return response.read()



def unquote_URL(path):
    return urllib.unquote(path)


