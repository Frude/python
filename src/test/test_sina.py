# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from GetSoup import Soup
from bs4 import BeautifulSoup
from apicloud.dataCloud import DataCloud
from Get_html import get_html
from StringIO import StringIO
import gzip
from upload import upload
from time import ctime
'''
Created on 2016-3-24

@author: Administrator
'''
def sina_news(cname,url,rela_chan):
    headers={
        'Accept':'image/webp,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
    #    'Host':'i.sso.sina.com.cn',
    
        'Referer':'http://news.sina.com.cn/s/qw/2016-03-24/doc-ifxqswxn6362654.shtml',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }
    print type(headers)
    #url= 'http://roll.news.sina.com.cn/news/shxw/qwys/index.shtml'#奇闻
    #url='http://roll.finance.sina.com.cn/finance/jj4/index_1.shtml'#基金
    sina =Soup(url,'gbk').get_soup()
    #print sina
    
    news_list = sina.find('ul',class_="list_009").find_all('li',limit =10)
    for news in news_list:
        new_url =news.a['href']
        print new_url
        title= news.a.get_text()#.encode('gbk')
        print title
    
        html = get_html(new_url, 0,False,False)
        soup =BeautifulSoup(html,'html.parser')
        content = str(soup.find('div',class_="article article_16"))
        #print content
        imgs ='http://imgsrc.baidu.com/baike/pic/item/dbb44aed2e738bd44be39fb6a08b87d6267ff973.jpg'
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
              "type" : "txt" 
            }  
        upload(data)
        print '*********************************'
        
print "in sina_news. %s"%(ctime())
def Sina_news():
    list =[
           #{"cname":"头条历史","url":'http://toutiao.com/news_history/',"rela_chan":'56f8ec1c1675c45d431adc5f'},
           {"cname":"新浪财经","url":"http://roll.finance.sina.com.cn/finance/jj4/index_1.shtml","rela_chan":'56f93be7508421125656a612'},
           {"cname":"新浪奇闻","url":"http://roll.news.sina.com.cn/news/shxw/qwys/index.shtml","rela_chan":'56f93be68cbdb5ce20604c1e'},
           ]
    for item in list:
        cname =item['cname']
        url =item['url']
        rela_chan =item['rela_chan']
        sina_news(cname,url,rela_chan)
    print "out sina_news. %s"%(ctime())
Sina_news()