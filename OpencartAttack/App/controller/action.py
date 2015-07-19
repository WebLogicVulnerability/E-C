#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''
from App.core.parse.parseworkflow import analyze_workflow
from App.core.parse.parseroute import get_current_route,get_config_route
from App.controller.web_client import exe_the_same_workflow
from App.core.pattern.attack import changeprice,set_data
from App.controller.__init__ import initialize
from App.controller.data import data_set, param_list

if __name__ == '__main__':
    initialize()
    analyze_workflow(get_current_route()+"\Graph4.dot")
    #exe_the_same_workflow()
    #changeprice()
    print param_list
    print data_set
    changeprice()
