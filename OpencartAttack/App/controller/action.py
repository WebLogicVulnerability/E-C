#coding:utf-8

'''
Created on Apr 26, 2015

@author: 
'''
from App.core.parse.parseworkflow import analyze_workflow
from App.core.parse.parseroute import get_current_route
from App.controller.web_client import exe_the_same_workflow
from App.controller.__init__ import initialize

if __name__ == '__main__':
    #initialize()
    analyze_workflow(get_current_route()+'Graph4.dot')
    print get_current_route()
    print 'analyse done'
    exe_the_same_workflow()
    
    #changeprice()
    #minusamount()
    #priceoverflow()