from test.upload import upload
from bs4 import BeautifulSoup
import requests
def fix_tieba(content):
    soup=BeautifulSoup(content,"lxml")
    iiii=soup.find("img",class_="BDE_Image")
    print iiii['src']
    m=0
    if m==0:
        m_head=soup.find("style")
        re_con=str(m_head)
        title=soup.find("div",class_="bc p")
        t_list=title.find_all("a")
        if t_list:
            for a in t_list:
                a_txt=a.get_text(strip=True)
                a.replace_with(a_txt)
        re_con+=str(title)

        m+=1
    text=soup.find_all("div",class_="i")
    if text:
        for i in text:
            a_list=i.find_all("a")
            for a in a_list:
                a_txt=a.get_text(strip=True)
                a.replace_with(a_txt)
            re_con+=str(i)
    return re_con
def fix_content(data):
    content=data["content"]
    tag=data["tag"]
    if tag=="tieba":
        fix_tieba(content)

url="http://tieba.baidu.com/mo/m?kz=4352722210&is_bakan=0&lp=5010&pinf=1_2_0"
content=requests.get(url)
#print content.text
content= fix_tieba(content.text)
data = {
      "id":"57684dcc15a630af1876012c",
      "title" : '134',
      "content" :content
}
upload(data,is_update=True)