#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
from App.controller.web_client import test_simple
from App.controller.data import param_list,price,num,data_set
from copy import deepcopy


def set_data(p_name,p_value):
    #设定测试用例中的post参数
    flag=False
    data_set=deepcopy(param_list)
    for p in data_set:
        p_copy=deepcopy(p)
        s=p_copy.find(p_name)
        if (s>0):
            flag=True
            e=s+len(p_name)+3
            p_copy=p_copy[e+2:]
            e2=p_copy.find('^_^')
            value=p_copy[0:e2]
            print value
            print p_value
            p=p.replace(value.__str__(),p_value.__str__())

    if (flag==True):
        print 'set data success'
    else:
        print 'doesn\'t find pointed data'
# three kinds of simple vulnerability####################################################
def changeprice():
    #遍历实际请求中的参数是否在攻击参数集合内
    #data_set=deepcopy(param_list)
    print param_list
    print data_set
    flag=False
    for pri in price:
        #print 'pri',pri
        for param in data_set:
            if pri in param:
                print 'settiondata......'
                set_data(pri,1)
                flag=True

    if flag==False:
        print 'it seems that we don\'t have that price parameter in our knowledge base'
    else:
        print 'testing change price'
        test_simple()
    
def minusamount():
    flag=False
    for amount in num:
        for param in param_list:
            if amount in param:
                set(amount,-1)
                flag=True
                
    if flag==False:
        print 'it seems that we don\'t have that amount parameter in our knowledge base'
    else:
        print 'testing minus amount'
        pass
    
def priceoverflow():
    
    flag=False
    for pri in price:
        for param in param_list:
            if pri in param:
                set(pri,2147483648)            #32bit compiler
                flag=True

    if flag==False:
        print 'it seems that we don\'t have that price parameter in our knowledge base'
    else:
        print 'testing price overflow'
        pass
#############################################################################################    
    
