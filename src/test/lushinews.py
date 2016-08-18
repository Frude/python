# -*- coding:UTF-8 -*-
from GetSoup import Soup
import re
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from upload import upload
from random import random
from time import ctime,sleep
'''
Created on 2016-4-17

@author: Administrator
'''
def fix_img(content,url):
    imgs=content.find_all('img')
    if imgs!=None:
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    video =content.find("embed")
    if video: 
        content=''
    return str(content)
def lushinews(cname,url,rela_chan):
    lushinews =get_html(url, -1,False,True)
    #print lushinews
    news_list = lushinews.find_all('div',class_="news-item",limit =10)
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        a=news.find("a")
        new_url =a['href']
        new_url=str(new_url).strip()
        print new_url
        imgs ='http://t10.baidu.com/it/u=3597010977,1595856409&fm=58'
        print imgs
        title=a.get_text()#.encode('gbk')
        print title
        soup2=Soup(new_url).get_soup()
        content= soup2.find('div', class_="article-con")
        content = fix_img(content,new_url)
        #print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : cname, 
              "url" : new_url, 
              "rela_chan" : rela_chan, 
              #56f93be68cbdb5ce20604c1e#qiwen
              #56f93be7508421125656a612#caijin
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "simg"
        }
        upload(data)
        print '*********************************'
print "in lushinews. %s"%(ctime())
def Lushinews():
    list =[
           #{"cname":"未解之谜","url":"http://www.83133.com/weijiezhimi/","rela_chan":'571340d4975f6bf2044eeea9'},
           {"cname":"炉石动态","url":"http://lushi.163.com/","rela_chan":'57135675a7a093606c6499cf'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        lushinews(cname,url,rela_chan)
    print "out lushinews. %s"%(ctime())
Lushinews()