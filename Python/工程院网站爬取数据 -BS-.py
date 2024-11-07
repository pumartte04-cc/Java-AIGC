from bs4 import BeautifulSoup
import re
import requests

baseurl = "https://www.cae.cn/cae/html/main/col48/column_48_1.html"
def getdata(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        return response.content.decode("utf-8")
    except requests.RequestException as e:
        print(f'Error for catching page:{e}')
        return None

text=getdata(baseurl)
soup=BeautifulSoup(text,'html.parser')
#print(soup.prettify())
section_title = "信息与电子工程学部"
section=soup.find(text=re.compile(section_title))
if section:
    print(f'Found->{section_title}')
    academicians_list = section.find_parent().find_next_sibling()
    #find_parent()找到它的父元素，接着使用find_next_sibling()查找下一个兄弟元素
    senior_academicians_list=section.find_parent().find_next_sibling().find_next_sibling().find_next_sibling()
    academicians = []
    senior_academicians=[]
    for item in academicians_list.find_all('li'):
        academicians.append(item.get_text(strip=True))
    print("院士名单:")
    for name in academicians:
        print(name)
    print(f'\n')
    for items in senior_academicians_list.find_all('li'):
        senior_academicians.append(items.get_text(strip=True))
        #strip=true ->remove any leading and trailing whitespace from the resulting string. 
        # This includes spaces, tabs, and newline characters.
    print("资深院士名单:")
    for names in senior_academicians:
        print(names)
