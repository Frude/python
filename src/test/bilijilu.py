# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from GetSoup import Soup
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from StringIO import StringIO
import gzip
from time import sleep
from random import random
def bilibili(url):
    baseURl ="http://www.bilibili.com"
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
               'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3', \
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',\
               'Host':'www.bilibili.com', \
               'Accept-Encoding':'gzip, deflate', \
               'Cache-Control':'max-age=0', \
               'Connection':'keep-alive'}
    
    request = urllib2.Request(r'http://www.bilibili.com/video/tech-popular-science-1.html#!page=1&order=hot&range=2016-03-16%2C2016-03-23', headers=headers)
    
    html = urllib2.urlopen(request)
    
    if html.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(html.read())
        f = gzip.GzipFile(fileobj=buf)
        html = f.read()
    #print html
    soup = BeautifulSoup(html,"html.parser")
    parents = soup.find('ul',class_="vd-list l1").find_all('li',limit=10)
    #print parents
    for parent in parents:
        print "**************************************"
        seconds=random()*5
        print seconds
        sleep(seconds)
        title = parent.div.a.img['alt']
        print title
        imgs = parent.div.a.img['data-img']
        print imgs
        newurl =baseURl +parent.div.a['href']
        print newurl
        print parent.div.div.div.get_text()
        print parent.find('div' ,class_="up-info").get_text("<br />")
        content = u''
        content+=u'''<img src="'''+imgs+'''" height='100%' width = '100%'>'''
        content+=u'<br />  '+parent.div.div.div.get_text()
        content+=u'''<br />视频地址：<a href="'''+newurl+u'''">点击这里</a>'''

        content+=u'<br />'+parent.find('div' ,class_="up-info").get_text("<br />")
        data = {
               "title" : title,
               "content" :content, 
               "imgs" : imgs,
               "cname" : "bilibili纪录片", 
               "url" : newurl, 
               "rela_chan" : '56f8ec188ecd71212f0768ec', 
               "is_hot" : 1, 
               "is_bot" : 1, 
               "type" : "simg"
            }  
        upload(data)
        print '*********************************'
# bilibili("url")

