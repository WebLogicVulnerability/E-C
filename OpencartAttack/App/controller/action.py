#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''
from App.core.parse.parseworkflow import analyze_workflow,get_post_data
from App.core.parse.parseroute import get_current_route,get_config_route
from App.controller.data import param_list
from App.controller.web_client import exe_the_same_workflow

if __name__ == '__main__':
#initialize
    analyze_workflow(get_current_route()+"\Graph4.dot")
    exe_the_same_workflow()
