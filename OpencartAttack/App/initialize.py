#coding:utf-8
from App.controller.data import PATH
from App.core.parse.parseroute import get_current_route
from App.core.parse.parseworkflow import analyze_workflow
from App.controller.graph_generator import generate_graph
from App.controller.web_client import check_the_workflow
from App.core.pattern.bypasspay import judge


import os

def check_dot_file():
    graph=open(get_current_route()+"Graph.dot",'r')
    data=graph.readline()
    if len(data)==0:
        print 'dot file seems be empty,please rerunning the workflow'
        
def try_workflow():
    print 'try workflow'
    analyze_workflow(get_current_route()+'Graph.dot')
    check_the_workflow()
    judge()
def _initialize():
    print 'initialize......'
    PATH= get_current_route()
    print 'path initialize success'
    trace_path = PATH+'trace.txt'
    print trace_path
    if os.path.exists(trace_path):
        pass
    else:
        print 'trace file seems don\'t exists,please check'
        exit
    print 'trying to generate graph......'
    generate_graph(trace_path)
    print 'graph generated'
    check_dot_file()
    try_workflow()
    print 'workflow can be exe rightly'
    
    