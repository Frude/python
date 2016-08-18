# -*- coding:UTF-8 -*-
from GetSoup import Soup
from upload import upload
def Bi():
    soup = Soup('http://www.businessinsider.com/').get_soup()
    parents =soup.find_all('div',class_='border-bottom',limit=10)
    for parent in parents:
        print "**************************************"
        if parent.h2==None:continue
        title=parent.h2.get_text(strip=True)
        imgs=parent.img['src']
        print title
        print imgs
        new_url=parent.h2.a['href']
        print new_url
        soup2=Soup(new_url).get_soup()
        contents= soup2.find('div', class_="KonaBody post-content")
        lese =contents.find('div' ,class_="related-links-container minimal ks-see-also")
        if lese!=None: 
            lese.extract() 
        content =''
        for i in contents:  
            if i ==lese :continue      
            content+=str(i)
        data = {
              "title" : title,
              "content" :content, 
              "imgs" : imgs,
              "cname" : "Business Insider", 
              "url" : new_url, 
              "rela_chan" : '56f8ec176ae45e231236b2a9',
              "is_hot" : 1, 
              "is_bot" : 1, 
              "type" : "img"
            }  
        upload(data)
        print '*********************************'
# Bi()


