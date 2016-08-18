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
#     div = content.div
#     if div:div.extract()
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
def xiancheng(cname,url,rela_chan):
    #lushinews2 =get_html(url, -1,False)
    xiancheng=get_html(url, 0, False, True)
    #print xiancheng
    #print lushinews
    base_url =url
    news_list = xiancheng.find('ul', id="new_list").find_all("li")
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        new_url =base_url+str(news.h2.a['href'])
        new_url=str(new_url).strip()
        print new_url
        imgs =news.find("img")['src']
        print imgs
        title=news.h2.a.get_text(strip=True)
        print title
        soup2=Soup(new_url,"").get_soup()
        contents =soup2.find_all("div" ,class_="artcile-detail")
        content= ""
        for i in contents:
            content+=str(fix_img(i))
        content += fix_img(soup2.find('div', class_="bdiv shop-msg"))
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
        upload(data,True,True)
        print '*********************************'
print "in xiancheng. %s"%(ctime())
def Weibo():
    list =[
           #{"cname":"未解之谜","url":"http://www.83133.com/weijiezhimi/","rela_chan":'571340d4975f6bf2044eeea9'},
           {"cname":"微博","url":"http://hangzhou.51xiancheng.com/","rela_chan":'57135675a7a093606c6499cf'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        xiancheng(cname,url,rela_chan)
    print "out xiancheng. %s"%(ctime())