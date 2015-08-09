#-*-coding:utf-8-*
'''
Created on 2015��5��2��

@author: Administrator
'''
import urllib 
import urllib2
send_headers = {
 'Host':'www.jb51.net',
 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'
}
def post(url, data):  
    req = urllib2.Request(url,headers=send_headers)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return response.read()
if __name__ == '__main__': 
    data={'city': 'jinan', 'fax': '', 'customer_group_id': '1', 'firstname': 'y_', 'lastname': 'hp_',  'country_id': '44', 'telephone': '13000000000', 'zone_id': '702', 'address_1': 'shandongjinanshunhualu', 'address_2': '', 'company': '', 'email': '111%40111.com', 'postcode': '250000'}
    url="http://211.87.234.178/index.php?route=checkout/guest/save"
    response=post(url,data)
    print response