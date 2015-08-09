#-*-coding:utf-8-*
'''
Created on 2015Äê8ÔÂ3ÈÕ

@author: Administrator
'''

from App.controller.data import PATH
from App.core.parse.parseroute import get_current_route


count_get=0
count_referer=0

loc_post=[]

t=1
def generate_graph(trace_path):   
    nodes=[]
    node={} 
    shop=open(trace_path,"r")
    line = shop.readline()

    while line:
    
        if 'GET' in line or 'Host' in line or 'POST' in line or '$_$' in line:
            if 'GET ' in line :
                temp=line.split()
                if node:  
                    nodes.append(node)
                    node={}
                node['GET_or_POST']='g'
                node["URL"]=temp[1]
            if 'POST ' in line: 
                temp_post=line.split()
    
                if node:  
                    nodes.append(node)#
                    node={}#
                        
                node['GET_or_POST']='p'
                node["URL"]=temp_post[1]
                node["pd"]='Y'
            if 'Host:' in line :
                s=line.rstrip()+node["URL"]
                node["URL"]=s[5:]
    
            if  node['GET_or_POST']=='p':  
                node['post_data']=''
            if "$_$" in line:
                    print 'post_data_line',line
                    node['post_data']=line
        else: 
            pass
                    
        line=shop.readline()
        aheadline=line
    
    if node['GET_or_POST']!='null':
        nodes.append(node)
    
    shop.close()
    
    a=0
    for nodes_num in range(0,len(nodes)):
        for order in range(0,nodes_num):
            if "Referer" in nodes[nodes_num] and "URL" in nodes[order] and nodes[order]["URL"] == nodes[nodes_num]["Referer"]:
                if "sons" in  nodes[order]:
                    nodes[order]["sons"].append(nodes_num)
                else:
                    nodes[order]["sons"]=[nodes_num]
    graph=open(get_current_route()+"Graph.dot",'w')
    
    graph.write("digraph shili1{\n")
    i=0
    for nodes_num in range(0,len(nodes)): 
        graph.write("p")
        graph.write(str(nodes_num))
        graph.write(" -> ")
        graph.write("p")
        graph.write(str(nodes_num+1))
        
        if nodes[nodes_num]["GET_or_POST"]=='p':
            graph.write(' [style="dashed",label="')
        else:   
            graph.write(' [label="')
    
        if "URL" in nodes[nodes_num]:
            graph.write(nodes[nodes_num]["URL"])
    
        if nodes[nodes_num]["GET_or_POST"]=='p':
            graph.write('"];'+'//')
            graph.write(nodes[nodes_num]["post_data"])
            print 'post data',nodes[nodes_num]["post_data"]
        
        else:
            graph.write('"];')
        
        graph.write('\n')
        print 'nodesnumner' ,nodes_num,nodes[nodes_num]["URL"]
    graph.write("}")
    print 'done'
    
    graph.close()

