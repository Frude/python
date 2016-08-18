# -*- coding:UTF-8 -*-
import feedparser
from bs4 import BeautifulSoup

def get_content(contents):
    if contents!=None:
        s=contents.find('p', class_='post-copyright')
        if s:s.extract()
        imgs=contents.find_all("img")
        for img in imgs:
            if img:
                img['height']='100%'
                img['width']='100%'
        return contents
    else:
        return ""
        


#d = feedparser.parse('http://ued.taobao.com/blog/feed/')
#http://lufuli.net/feed/
d = feedparser.parse('http://ued.taobao.com/blog/feed/')

for item in d.entries:
    print "************************************************************"
    print 'title = %s' % (item.title,)
    title=item.title
    print 'link = %s' % (item.link,)
    new_url=item.link
    #print item.content[0].value
    for i in item.content:
        soup=BeautifulSoup(i.value,"html.parser")
        print soup.find("img")
        print get_content(soup)
    data = {
              "title" : title,
              "content" :contents, 
              "imgs" : imgs,
              "cname" : "撸福利", 
              "url" : new_url, 
              "rela_chan" : '56f8ec1ced37c342644271e0', 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "img"
            }  
    upload(data)
    print "************************************************************"

    
    