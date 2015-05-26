#coding:utf-8
'''
Created on 2015年5月25日

@author: Administrator

'''
#新的类替换auto_visitor，有太多方法需要定义所以新建类
import os
import urllib 
import urllib2
import cookielib
import re

def web_client():
    data={}  
    get_url_param("G://Graph4.dot")
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
