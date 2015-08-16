#-*-coding:utf-8-*
'''
Created on 2015��8��2��

@author: Administrator
'''
from App.controller.data import url_list,param_list,pay_page,order_placed_page
from App.core.parse import parseurl
from copy import deepcopy
from App.controller.web_client import post
import ssl
import cookielib
import urllib2
def judge():
    urllist=deepcopy(url_list)
    current=urllist.pop()
    while (urllist):
        next=urllist.pop()
        if current != next:
            pay_page=next
            current=next
            break
        else:
            current=next
    while (urllist):
        next=urllist.pop()
        if current != next:
            order_placed_page=next
            break
        else:
            current=next
def find_data():
    count=0
    for url in url_list:
        if url!=url_list[count]:
            count=count+1
    return count
def bypasspay():
    ssl._create_default_https_context = ssl._create_unverified_context
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    count=find_data()
    html=post(url_list[count],param_list[count],opener)  
    #check similarity  