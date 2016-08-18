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
from time import ctime,sleep
from random import random
import time

import sys

reload(sys)

def fix_img(content):
    if(content==None):return ''
    if type(content)==str: return content
#     sections=content.find_all("section")
#     if sections:#sections.decompose()
#         for section in sections:
#             section.decompose()
    imgs=content.find_all('img')
    if imgs!=None:
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    return str(content)

def tengxunxinwen(cname,url,rela_chan):
    baseURl = 'http://ent.qq.com'
#     html = get_html(url,3)
#     soup = BeautifulSoup(html,"html.parser")
    soup=Soup(url,"").get_soup()
    #print soup
    parents =soup.find_all("div", class_="nrC",limit =10)
    
    for parent in parents:
        print "**************************************"
        seconds=random()*5
        print seconds
        time.sleep(seconds)
        newurl =baseURl+parent.a['href']
        print newurl
        imgs = parent.find("img")
        if  not imgs : 
            imgs = "http://mat1.gtimg.com/www/images/channel_logo/ent_logo.png"
            #title = parent.h3.a.get_text(strip=True)
        else : 
            #title = parent.h3.a.get_text(strip=True).decode()#.encode("gb2312")
            imgs=imgs['src']

        print imgs
        
#         print title
        soup2=Soup(newurl,"gbk").get_soup()
        #print soup2
        
        title = soup2.find("div" ,class_="qq_article")
        if title : title=title.div.h1.get_text(strip=True)
        print title
        content=  soup2.find("div",id="Cnt-Main-Article-QQ")
        content = fix_img(content)
        #print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" :cname, 
              "url" : newurl, 
              "rela_chan" : rela_chan, 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg"
            }  
        upload(data)#,True,True)
        print '*********************************'

print "in tengxunxinwen. %s"%(ctime())
def TengxunNews():
    list =[
           #{"cname":"头条历史","url":'http://toutiao.com/news_history/',"rela_chan":'56f8ec1c1675c45d431adc5f'},
           {"cname":"综艺新闻","url":"http://ent.qq.com/tv/tvxw/zyxw/zykb.htm","rela_chan":'5720d1dd3e4ef78002c67c96'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        tengxunxinwen(cname,url,rela_chan)
    print "out tengxunxinwen. %s"%(ctime())
# TengxunNews()
