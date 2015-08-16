#-*-coding:utf-8-*

'''
Created on Apr 26, 2015

@author: Administrator
'''

from App.initialize import _initialize
from App.core.pattern.bypasspay import bypasspay
from App.core.pattern.changeprice import changeprice
from App.core.pattern.minusamount import minusamount
from App.core.pattern.priceoverflow import priceoverflow
from App.core.pattern.switchsession import switch_session
from App.core.pattern.switchsid import switch_sid

from App.core.pattern.attack import set_vul
if __name__ == '__main__':
    _initialize()    
    check = set_vul()
#     for option in check:
#         if check[option]=='y':
#             if option == 'cp':
#                 changeprice()
#             elif option == 'ma':
#                 minusamount()
#             elif option == 'po':
#                 priceoverflow()
#             elif option == 'ss':
#                 switch_sid()
#             elif option == 'sse':
#                 switch_session()
#             elif option == 'bp':
#                 bypasspay()

