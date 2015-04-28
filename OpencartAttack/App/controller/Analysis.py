#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''
import os

#返回指定配置文件的内容
def getconfigRoute():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]+"\conf\config.txt"
    return route
    
if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words