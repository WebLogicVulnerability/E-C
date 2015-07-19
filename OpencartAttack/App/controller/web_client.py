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
from data import url_list
from data import param_list
from App.core.parse.parseworkflow import get_url_param,get_post_data

def get(url,opener):
    resp = opener.open("http://"+url);   
    return resp

def post(url, data,opener):  
    url="https://"+url
    data = urllib.urlencode(data)  
    req=urllib2.Request(url,data)
    response = opener.open(req)
    return response

def get_current_route():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]
    return route

def getconfigRoute():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]+"\conf\config.txt"
    return route

def test_session():
    
    def session1():
        print 'session1'
        get_url_param(get_current_route()+"\Graph4.dot")
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
        get_url_param(get_current_route()+"\Graph4.dot")
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
    get_url_param(get_current_route()+"\Graph4.dot")
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

