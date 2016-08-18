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
    if(content==None):return ''
    if type(content)==str: return content
    sections=content.find_all("section")
    if sections:#sections.decompose()
        for section in sections:
            section.decompose()
    imgs=content.find_all('img')
    if imgs!=None:
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
    return str(content)
def healthsina(cname,url,rela_chan):
    #url='http://news.yodao.com/search?q=每日轻松一刻'
    #healthsina =get_html(url, -1, False)
    #print healthsina
    #sina_1 = get_html(url,5,is_img=True,is_soup=True)
    sina_1 =Soup(url,"").get_soup()
    #print sina_1
    
    #news_list = sina_1.find_all("li" ,class_="clearfix",limit=1)
    news_list = sina_1.find_all('div' ,class_="traSlideCon alls onhappen" ,limit=1)
    print news_list
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        h3=news.find('h3')
        new_url =h3.a['href']
        print new_url
        imgs = news.a.img['src']
        print imgs
        title= h3.a.get_text(strip=True)
        print title
        #soup2=get_html(new_url,4,False,True)
        soup2=Soup(new_url,"").get_soup()
        #print soup2.body
        content =soup2.find('section' ,class_="art_main_card j_article_main")
        #print content
        content= fix_img(content)
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
              "type" : "img"
        }
        #upload(data)
        print '*********************************'
    
print "in healthsina. %s"%(ctime())
def HealthSina():
    list =[
           #{"cname":"新浪旅游","url":"http://travel.sina.com.cn/","rela_chan":'571340d4975f6bf2044eeea9'},
           {"cname":"新浪健康","url":"http://health.sina.cn/healthcare/index.d.html?vt=4&pos=42","rela_chan":'57173f3d5fefa0ce23755183'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        healthsina(cname,url,rela_chan)
    print "out healthsina. %s"%(ctime())