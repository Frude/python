# -*- coding:UTF-8 -*-
from GetSoup import Soup
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
def Wangyi_news():
    print "in wangyi_news. %s"%(ctime())
    url='http://digi.163.com/keywords/9/d/9ed179d16280/1.html'
    net_easy =Soup(url,'gbk').get_soup()
    #print net_easy
    
    news_list = net_easy.find('ul', id="content").find_all('li',limit =10)
    for news in news_list:
        print '*********************************'
        seconds=random()*5
        print seconds
        sleep(seconds)
        item =news.find('a',class_="newsList-img" )
        new_url =item['href']
        print new_url
        title= item.img['alt']#.get_text()#.encode('gbk')
        print title
        soup2=Soup(new_url,'gbk').get_soup()
        content= str(soup2.find('div', class_="post_text", id="endText"))
        imgs =item.img['src']
        print imgs
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "网易黑科技新闻", 
              "url" : new_url, 
              "rela_chan" : '5713219a975f6bf2044eed0f', 
              #56f93be68cbdb5ce20604c1e#qiwen
              #56f93be7508421125656a612#caijin
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "img"
        }
        upload(data)
        print '*********************************'
    print "out wangyi_news. %s"%(ctime())
# Wangyi_news()