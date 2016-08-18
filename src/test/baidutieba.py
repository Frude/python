# -*- coding:UTF-8 -*-
'''
Created on 2016-2-28

@author: Administrator
'''
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from datetime import * 
from GetSoup import Soup
from apicloud.dataCloud import DataCloud
from upload import upload
from random import random
from time import ctime, sleep
import threading
from test import Get_html
from test.Get_html import get_html

def tieba(url,text,rela_chan):
    print "in "+text+"  at "+ctime()
    data = {
              "title" : 'title',
              "content" :'', 
              "imgs" : 'http://t11.baidu.com/it/u=3490412254,2087462657&fm=58',
              "cname" : text+"吧", 
              "url" : "", 
              "rela_chan" : rela_chan, 
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "txt"
    }       
    #http://tieba.baidu.com/f?kw=%CA%E9%BB%C4&fr=ala0&loc=rec'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read()
        soup = BeautifulSoup(content,"html.parser")
        x=0   
        for link in soup.find_all('a',class_='j_th_tit',limit=11):
            print "******************************************************"
            seconds=random()*5
            print seconds
            sleep(seconds)
            x+=1
            if x<=3 :continue
            #raw_input("Press Enter to continue...")    
            #wait()
            page=1
            max_page=1
            data['url']='http://tieba.baidu.com'+link['href']
            print data['url']
            while(page<=max_page):
                # 暂时没有只见楼主
                baseURL = 'http://tieba.baidu.com'+link['href']+"?pn="+str(page)
                #print baseURL
#                 request2 = urllib2.Request(baseURL,headers = headers)
#                 response2 = urllib2.urlopen(request2)
#                 content2 = response2.read()#.decode('utf-8')
#                 soup2 = BeautifulSoup(content2,"html.parser")
                soup2=get_html(baseURL, 0, False, True)
                max_page1 = soup2.find('li' ,class_="l_reply_num")
                if max_page1 :max_page1=max_page1.get_text()
                else : max_page=1
                max_page=int(re.findall("\d+",max_page1).pop())
                if max_page>20:max_page=20
                #print max_page
#                 if page ==1 :
#                     img=soup2.find("img", class_="BDE_Image")
#                     print img
                page+=1 
                for content in soup2.find_all('div',{'class':'d_post_content j_d_post_content '}):
                    #print content.get_text()
                    data['content']+='**************************************************<br />'
                    #print data['content']
                    imgs=content.find_all("img", class_="BDE_Image")
                    for imgg in imgs:
                        if imgg:
                            imgg['height']='100%'
                            imgg['width']='100%'
                            #print imgg
                            #data['content']+=imgg.decode()+u'<br />'
                    data['content']+=str(content)+'<br />'
                data['content']+='<br />**************************************************<br />'
#             if img :
#                 data['imgs']=img['src']
#             else :
#                 data['imgs']="http://imgsrc.baidu.com/forum/pic/item/2834349b033b5bb5c50c5c6434d3d539b700bc54.jpg"
            
            title=soup2.find('h3').get_text(strip=True)
#             print "yuan shi title: "+title
            if re.match(u"回复：", title):
                title=re.sub(u"回复：",u"",title)
            data['title']=title
            print data['title']
            upload(data)
            data['content']=""
            print "******************************************************"
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    print "out "+text+"  at"+ctime()
def Tieba():
    print "in tieba  at "+ctime()
    list =[
#         {"rela_chan":'56f9437a27b94d9119fcf054',"text":"书荒"},
#         {"rela_chan":'56f941c66ae45e231236b611',"text":"dnf"},
#         {"rela_chan":'56f8ec1c6ae45e231236b2aa',"text":"太子妃升职记"},
        {"rela_chan":'573b53fe8e269a8943b3d450',"text":"绿帽小同学"},
    #        {"text":"书荒","rela_chan":'56f9437a27b94d9119fcf054'},
    #        {"text":"书荒","rela_chan":'56f9437a27b94d9119fcf054'},
    #        {"text":"书荒","rela_chan":'56f9437a27b94d9119fcf054'},    
        ]
    # item ={"text":"书荒","rela_chan":'56f9437a27b94d9119fcf054'}
    # if item in list:
    #     text=item["text"]
    #     url =" http://tieba.baidu.com/f?ie=utf-8&kw="+text+"&fr=search"
    #     rela_chan = item["rela_chan"]
    #     tieba(url,rela_chan)
    # else :
    #     print "not find!!"
#     for item in list:
#         text=item["text"]
#         url =" http://tieba.baidu.com/f?ie=utf-8&kw="+text+"&fr=search"
#         rela_chan = item["rela_chan"]
#         tieba(url,text,rela_chan)
    threads = []
    for item in list:
        text=item["text"]
        url =" http://tieba.baidu.com/f?ie=utf-8&kw="+text+"&fr=search"
        rela_chan = item["rela_chan"]
        t = threading.Thread(target=tieba,args=(url,text,rela_chan,))#lufuli.Lufuli,args=("zhainafuli/",))
        #toutiao(cname,url,rela_chan)
        threads.append(t) 
    for t in threads:
#         t.append()
        t.setDaemon(True)
        t.start()
        time.sleep(5)
    for t in threads:
        t.join()
    print "all over %s" %ctime()
    print "out tieba at "+ctime()
# Tieba()