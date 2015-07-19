#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
import os
def get_current_route():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]
    return route

def get_config_route():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]+"\conf\config.txt"
    return route
