#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''

from web_client import getconfigRoute
from web_client import auto_visiter
from web_client import test_session


if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    
    #auto_visiter()
    test_session()
