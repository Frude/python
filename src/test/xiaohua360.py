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
def fix_img(content):
    imgs=content.find_all('img')
    if imgs!=None:
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    return str(content)
def xiaohua360(cname,url,rela_chan):
    #url='http://news.yodao.com/search?q=每日轻松一刻'
    xiaohua360 =Soup(url).get_soup()
    #print xiaohua360
    
    news_list = xiaohua360.find_all('div', id="img-list",limit =10)
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        h3=news.find('h3')
        new_url =h3.a['href']
        print new_url
        imgs =news.find('img').get("src")
        print imgs
        title= h3.get_text().encode("utf-8")
        print title
        soup2=Soup(new_url).get_soup()
        content =soup2.find('div', class_="doc-main box")
        content= fix_img(content)
        #print content
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : cname, 
              "url" : new_url, 
              "rela_chan" : rela_chan, 
              #571340d4975f6bf2044eeea9#weijiezhimi
              #56f93be7508421125656a612#caijin
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "img"
        }
        upload(data)
        print '*********************************'
def Xiaohua360():
    print "in xiaohua360. %s"%(ctime())
    list =[
           #{"cname":"未解之谜","url":"http://www.83133.com/weijiezhimi/","rela_chan":'571340d4975f6bf2044eeea9'},
           {"cname":"导姐叨叨叨","url":"http://xiaohua.360.cn/daojie","rela_chan":'57134f7ff14d017c08e2eff6'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        xiaohua360(cname,url,rela_chan)
    print "out xiaohua360. %s"%(ctime())
# Xiaohua360()