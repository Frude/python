# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
import sys
import os
from log.main import m_log
'''
Created on 2016-4-17

@author: Administrator
'''
def fix_img(content):   
    if(content==None):return ''
    if type(content)==str: return content
    noscripts=content.find_all('noscript')
    if noscripts==None: return str(content)
    for noscript in noscripts:
        imgs=noscript.find('img')
        if imgs!=None:
            for img in imgs:
                if img:
                    img['height']='100%'
                    img['width']='100%'
        noscript.replace_with(imgs)
    return str(content)
def guokr(cname,url,rela_chan):
    #url='http://news.yodao.com/search?q=每日轻松一刻'
    guokr =Soup(url).get_soup()
    #print guokr
    
    news_list = guokr.find('ul', class_="titles").find_all('li',limit=10)
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url =news.a['href']
        print new_url
        imgs ="http://img2.imgtn.bdimg.com/it/u=1604389173,2448055779&fm=21&gp=0.jpg"
        print imgs
        title= news.a.get_text(strip=True).encode('utf-8')
        print title
        soup2=Soup(new_url).get_soup()
        content1 =soup2.find('div',id="postContent")
        content2 =soup2.find('div',class_="document")
        #content3 =soup2.find('div', class_="main-video")
        content3 =soup2.find('article', class_="content-main question")
        content4 =None
        if content3:
            fenxiang=content3.find('div' ,class_="content-func-area")
            fenxiang.decompose()
            content4 =soup2.find('section',class_="content-block")
            content4=fix_img(content3)+"***************************************************"+fix_img(content4)
        content= fix_img(content1)+fix_img(content2)+fix_img(content4)
        #print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : cname, 
              "url" : new_url, 
              "rela_chan" : rela_chan, 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "txt",
        }
        upload(data)
        print '*********************************'
def Guokr():   
    file_name="guokr"
#     m_log(file_name)
    print "in %s. %s"%(file_name,ctime())
    list =[
           #{"cname":"未解之谜","url":"http://www.83133.com/weijiezhimi/","rela_chan":'571340d4975f6bf2044eeea9'},
           {"cname":"果壳","url":"http://m.guokr.com/","rela_chan":'571373a8168648fd68eb42d2'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        guokr(cname,url,rela_chan)
    print "out %s. %s"%(file_name,ctime())
# #     logfile.close()
# Guokr()