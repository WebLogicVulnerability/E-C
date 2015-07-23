#coding:utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_URL(html):
    url=r'href="(.+?)"'
    url_re = re.compile(url)
    url_listist = re.findall(url_re,html)
    return url_listist

#html = getHtml("http://www.freebuf.com/")
#print html
#for i in getURL(html):
#   print i