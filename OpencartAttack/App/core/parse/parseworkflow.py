#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
import re
from App.controller.data import url_list,param_list, url_set,data_set
from copy import deepcopy

def analyze_workflow(path):
    #������url��param���ֱ�洢������list��
    file_object = open(path)
    for line in file_object:
        #line�����http�������������
        url=param=""
        if(re.findall(r'label=\".*\"]',line).__str__()<>'[]'):
            #url���������ڵ�����
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
        url_set=deepcopy(url_list)
        data_set=deepcopy(param_list)
    return url_list,param_list,url_set,data_set

