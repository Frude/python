# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from datetime import *  
import time
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
def Huyashipin():
    url = 'http://v.huya.com/lol/'
    headers = {
        'User-Agent': "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)",
    #    'Host': "pinghot.qq.com",
        'Referer': "http://lol.qq.com/v/index.shtml",
        'X-Requested-With': "XMLHttpRequest"
            }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        contents = response.read()
        soup = BeautifulSoup(contents,"html.parser")
        parents =soup.find_all("div", class_="uiVideo__item",limit=10)
        for parent in parents:
            print '*********************************'
            content = u'''<img src="'''+parent.a.img['src']+'''" height='100%' width = '100%'>'''
            print content
            #content +=str(parent.a.img)
            print parent.a['href']
            url2=parent.a['href']
            request = urllib2.Request(url2,headers = headers)
            response2 = urllib2.urlopen(request)
            contents2 = response2.read()
            soup2 = BeautifulSoup(contents2,"lxml")
            #print soup2
            print soup2.find('div',class_='video-des').get_text(strip=True)
            #这是正文介绍
            content+=u'<br />  '+soup2.find('div',class_='video-des').get_text(strip=True)
            print parent.a.span.get_text()
            print parent.div.a.get_text()
            content+=u'''<br />视频地址：<a href="'''+parent.a['href']+u'''">点击这里</a>'''
            content+=u'<br />视频时间：'+parent.a.span.get_text()
            content+=u'<br />视频作者：'+parent.div.a.get_text()
            print parent.div.previous_sibling.previous_sibling.get_text()
            print parent.div.div.get_text()
            title = parent.div.previous_sibling.previous_sibling.get_text()
    
            imgs = str(parent.a.img['src'])
            data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "虎牙lol视频", 
              "url" : url2, 
              "rela_chan" : '56f8ec1c508421125656a2cf', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg"
              }   
            upload(data)
            print '*********************************'
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
# Huyashipin()
