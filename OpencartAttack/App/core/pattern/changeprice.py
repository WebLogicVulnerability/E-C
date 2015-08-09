#-*-coding:utf-8-*

'''
Created on 2015年7月25日

@author: Administrator
'''
from App.controller.web_client import test_simple
from App.controller.data import param_list,price,url_list
from copy import deepcopy
from attack import set_data
def check_change_price():
    pass
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
                #print '传递后的dataset',data_set
                flag=True

    if flag==False:
        print 'it seems that we don\'t have that price parameter in our knowledge base'
    else:
        print 'testing change price'
        test_simple(url_list,data_set)
    