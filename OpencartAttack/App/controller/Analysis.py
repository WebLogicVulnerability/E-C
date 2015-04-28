#coding:utf-8
'''
Created on Apr 26, 2015

@author: tonyzhou
'''
import os
#python字符串以及文件处理 http://www.jb51.net/article/47956.htm；http://www.cnblogs.com/zhoujie/archive/2013/04/10/python7.html

#返回指定配置文件的地址
def getconfigRoute():
    currentRoute=os.path.dirname(os.path.dirname(__file__))  
    route=currentRoute[:-4]+"\conf\config.txt"
    return route

if __name__ == '__main__':
    guide=getconfigRoute()
    conf=open(guide,'r')
    words=conf.read();
    print words