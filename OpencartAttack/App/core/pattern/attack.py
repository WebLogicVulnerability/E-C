#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
from App.controller.web_client import get,post
from App.controller.data import param_list,price,num
from copy import deepcopy
def changeprice():
    #遍历实际请求中的参数是否在攻击参数集合内
    flag=False
    param_list_copy=deepcopy(param_list)
    for param in param_list_copy:
        if param in price:
            flag=True
            param=1
    if flag==False:
        print 'it seems that we dont have that parameter in our knowledge base'
    else:
        pass
def minusamount():
    flag=False
    param_list_copy=deepcopy(param_list)
    for param in param_list_copy:
        if param in num:
            flag=True
            param=-1
    if flag==False:
        print 'it seems that we dont have that parameter in our knowledge base'
    else:
        pass
def priceoverflow():
    flag=False
    param_list_copy=deepcopy(param_list)
    for param in param_list_copy:
        if param in price:
            flag=True
            #32bit compiler
            param=2147483648
    if flag==False:
        print 'it seems that we dont have that parameter in our knowledge base'
    else:
        pass