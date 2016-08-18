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
def HH():
    baseURl = 'http://tx3.netease.com/thread-'
    html = get_html('http://tx3.netease.com/forum-38-1.html',0)
    soup = BeautifulSoup(html,"html.parser")
    #soup = Soup('http://tx3.netease.com/forum-38-1.html','').get_soup()
    #print soup
    parents =soup.find('table',summary="forum_38",id="threadlisttableid" ).find_all('tbody',id=re.compile("normalthread"),limit=13)
    #print soup.find('table',summary="forum_38",id="threadlisttableid" )
    
    for parent in parents:
        print "**************************************"
        num= re.findall(r"\d+\.?\d*",str(parent['id']))[0]
        i=1
        newurl = baseURl+num +"-"+str(i)+"-1.html"
        soup2 = Soup(newurl,'').get_soup()
        aa = soup2.find_all('td',class_="t_f")
        title = soup2.find('span' ,id="thread_subject").get_text()
        content = ''
        for a in aa:
            content+='<br />******************************************<br />'
            imgg =a.find_all('img')
            for img in imgg:
                if(img!=None and img.get('src')!="http://res.nie.netease.com/comm/blank.gif" and img.get('src')!=None):   
                    img['src']='http://tx3.netease.com/'+img['src']
                    print img
            content+=str(a)
            content+='<br />******************************************<br />'
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : 'http://img0.ph.126.net/WBCng-JL-jwSqR-9V5IWJg==/6630505915258888800.jpg',
              "cname" : "天下3荒火论坛", 
              "url" : newurl, 
              "rela_chan" : '56f8ec1627b94d9119fcecee', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "txt"
            }  
        upload(data)
        print '*********************************'
HH()

