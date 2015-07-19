'''
Created on 2015年7月19日

@author: Administrator
'''
import re
from App.controller.data import url_list,param_list

def get_url_param(path):
    #正则处理url和param并分别存储在两个list中
    file_object = open(path)
    for line in file_object:
        #line是整个http请求的所有内容
        url=param=""
        if(re.findall(r'label=\".*\"]',line).__str__()<>'[]'):
            #url是中括号内的内容
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
    #获得param_list中元素的值，存储在字典中并返回
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