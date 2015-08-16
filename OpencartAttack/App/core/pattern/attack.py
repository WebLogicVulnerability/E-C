#-*-coding:utf-8-*
'''
Created on 2015��7��19��

@author: Administrator
'''
from App.controller.web_client import test_simple
from App.controller.data import param_list,price,num,data_set, url_list,order_placed_page,sid,t_price,cookie,session
from copy import deepcopy
from App.controller.web_client import get_all_data

check={'bp':'n','cp':'n','ma':'n','po':'n','sse':'n','ss':'n'}


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



def set_vul():
    
    if order_placed_page:
        check.update('bp', 'y')
    params = get_all_data()
    for param in params:
        #print 'current_param',param
        if param in price:
            check['cp']= 'y'
        elif param in num:
            check['ma']= 'y'
        elif param in t_price:
            check['po']= 'y'
        elif param in sid:
            check['ss']= 'y'
            
    #check switch session
    for s in session:
        if s in cookie:
            check['sse']= 'y'
    #check bypass pay
    #if oder placed page exists 
    
    print 'folowing attack is going to be detected'
    for option in check:
        if check[option]=='y':
            if option == 'cp':
                print 'change price'
            elif option == 'ma':
                print 'minus amount'
            elif option == 'po':
                print 'price overflow'
            elif option == 'ss':
                print 'switch sid'
            elif option == 'sse':
                print 'switch session'
            elif option == 'bp':
                print 'bypass payment'
    return check


