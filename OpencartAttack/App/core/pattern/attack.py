#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
from App.controller.web_client import test_simple
from App.controller.data import param_list,price,num,data_set, url_list
from copy import deepcopy




def set_data(data_set,p_name,p_value):
    #设定测试用例中的post参数
    flag=False
    for p in data_set:
        p_copy=deepcopy(p)
        s=p_copy.find(p_name)
        if (s>0):
            flag=True
            e=s+len(p_name)+3
            p_copy=p_copy[e:]
            e2=p_copy.find('^_^')
            value=p_copy[0:e2]
            print '修改前的参数',p
            pp=p.replace(value.__str__(),p_value.__str__())
            data_set[data_set.index(p)]=pp
            print '修改后的参数',pp

    if (flag==True):
        print 'set data success'
        print '传递之前的dataset',data_set
        return data_set
    else:
        print 'doesn\'t find pointed data'



# three kinds of simple vulnerability####################################################
def changeprice():
    #遍历实际请求中的参数是否在攻击参数集合内
    data_set=deepcopy(param_list)
    print param_list
    print data_set
    flag=False
    for pri in price:
        #print 'pri',pri
        for param in data_set:
            if pri in param:
                print 'setting price data......'
                #set price 1
                data_set=set_data(data_set,pri,1)
                print '传递后的dataset',data_set
                flag=True

    if flag==False:
        print 'it seems that we don\'t have that price parameter in our knowledge base'
    else:
        print 'testing change price'
        test_simple(url_list,data_set)
    
def minusamount():
    data_set=deepcopy(param_list)
    print param_list
    print data_set
    flag=False
    for pri in num:
        #print 'pri',pri
        for param in data_set:
            if pri in param:
                print 'setting amount data......'
                #set account -1
                data_set=set_data(data_set,pri,-1)
                print '传递后的dataset',data_set
                flag=True

    if flag==False:
        print 'it seems that we don\'t have that price parameter in our knowledge base'
    else:
        print 'testing change price'
        test_simple(url_list,data_set)
        
def priceoverflow():
    data_set=deepcopy(param_list)
    print param_list
    print data_set
    flag=False
    for pri in price:
        #print 'pri',pri
        for param in data_set:
            if pri in param:
                print 'setting price data......'
                #set price 1
                data_set=set_data(data_set,pri,2147483648)
                print '传递后的dataset',data_set
                flag=True

    if flag==False:
        print 'it seems that we don\'t have that price parameter in our knowledge base'
    else:
        print 'testing change price'
        test_simple(url_list,data_set)
    
    
#############################################################################################    
    
