#-*-coding:utf-8-*
'''
@author: Administrator
'''
import difflib
#compute the similaruty of two html pages,return the percentage of similarity
def calculate_similarity(content1,content2):

    f=difflib.SequenceMatcher(None,content1,content2)
    s=0.00;
    for blocks in f.get_matching_blocks():
        if (blocks.size!=1):
            s=s+blocks.size
    return s/len(content1)


    