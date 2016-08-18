# -*- coding:UTF-8 -*-

import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup
from Save import Save
from GetSoup import Soup
from apicloud.dataCloud import DataCloud
from upload import upload
from time import ctime,sleep
from random import random
import time
from Get_html import get_html
def Hanzishang():
    url ='http://www.1mod.org/forum.php?mod=forumdisplay&fid=54&filter=author&orderby=dateline'
    html = get_html(url,0,False)
    soup = BeautifulSoup(html,"html.parser")
    #<tbody id="normalthread_157655">
    parents = soup.find_all('tbody',id=re.compile("normalthread"),limit=10)
    #print parents
    for parent in parents:
        print  "****************************************************************"
        seconds=random()*5
        print seconds
        time.sleep(seconds)
        title_tag=parent.find('a',class_="s xst")
        title= title_tag.get_text()
        new_url= title_tag['href']
        print title
        print new_url
        soup2 = Soup(new_url).get_soup()
    #     html = get_html(new_url,0)
    #     soup2=BeautifulSoup(html,"html.parser")
        contents= soup2.find_all('td' ,class_="t_f",id=re.compile("postmessage"))
        #print contents[0].get_text()
        text=""
        for content in contents:
            text+="**************************************************<br />"
            text+=content.get_text(strip=True)
            text+='<br />**************************************************<br /><br />'
        #print text
        data = {
          "title" : title,
          "content" :text, 
          "imgs" : "http://360fu.1mod.org/data/attachment/forum/201203/20/091224dezj7prhsd8pjlk6.jpg",
          "cname" : "汉之殇", 
          "url" : new_url, 
          "rela_chan" : '57172a1e917750330ca5fcfc', 
          "is_hot" : 1, 
          "is_bot" : 1, 
          "type" : "txt"
        }  
        upload(data)
        print '*********************************'
Hanzishang()
