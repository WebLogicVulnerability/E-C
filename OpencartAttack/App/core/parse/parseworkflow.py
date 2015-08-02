#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
import re
from App.controller.data import url_list,param_list
from copy import deepcopy

def analyze_workflow(path):
    file_object = open(path)
    for line in file_object:
        url=param=""
        if(re.findall(r'label=\".*\"]',line).__str__()<>'[]'):
            p = re.compile(r'(?<=label=\"\s).*(?=\"])')
            for m in p.finditer(line):
                url=m.group()
            url=url.replace('\\r','')
            p = re.compile(r'(?<=//).*')
            for m in p.finditer(line):
                param = m.group()
        if (param.__str__().find('$_$')>0):
            url_list.append(url)
            param_list.append(param)
        else:
            if(url<>""):
                url_list.append(url)
                param_list.append("")
    return url_list,param_list

