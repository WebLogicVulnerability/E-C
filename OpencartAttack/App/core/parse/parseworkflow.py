#coding:utf-8
'''
Created on 2015��7��19��

@author: Administrator
'''
import re
from App.controller.data import url_list,param_list

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
    return url_list,param_list

def get_post_data(param_list_element):
    #���param_list��Ԫ�ص�ֵ���洢���ֵ��в�����
    p=param_list_element
    data={}
    while(len(p)>1):
        s=0
        e=p.find("^_^")
        if(e>0):
            tem=p[s:e]
            s=e+3
            p=p[s:]
            e1=tem.find("$_$")
            s1=0
            name=tem[s1:e1]
            value=tem[e1+3:]
            data[name]=value      
        else:
            break
    return data