#正则表达式进行网页处理：地址http://www.purepen.com/hlm/的网站为红楼梦在线阅读网站，
# 请抓取该网站所有章节内容，将所有章节合成为txt文件并保存。
#https://www.runoob.com/python3/python-requests.html
import requests
#https://www.runoob.com/python/python-reg-expressions.html
import re
#查看工作目录，txt文件保存在哪里
#import os
#print(os.getcwd())

baseurl='http://www.purepen.com/hlm/'
all_contents=[]

#对HTML发出请求 用到 import request
def getpage(url):
    try:
        response=requests.get(url)  #发送请求
        response.raise_for_status()  #用于检查 HTTP 请求的响应状态码
        #print(response.apparent_encoding)  查看页面使用的是什么编码
        return response.content.decode("GB18030") #返回网页内容
    except requests.RequestException as e:
        print(f'Error exixts: {e}')
        return None

for i in range(1,121):
    chapter_url = f"{baseurl}{i:03}.htm"
    #print(chapter_url)
    x=getpage(chapter_url)  #x为获取到的网页内容
    titles=re.findall(r'<title>(.+?)</title>',x)  #在字符串中找到正则表达式所匹配的所有子串，并返回一个列表
    new_title = [re.sub(r"\u3000|\s+", '', title) for title in titles]  #去除\u3000以及其他空白字符
    bodys=re.findall(r'<FONT COLOR="#000000"  face="宋体" size="3">(.+?)</font>',x,re.S)
    new_body = [re.sub(r"\n|\u3000|\s+", '', body) for body in bodys]
    all_contents.extend([(title + '\n', body + '\n\n') for title, body in zip(new_title, new_body)])
    # 创建了一个新的列表。这个列表由元组组成，每个元组包含两个元素：（title + '\n'），（body + '\n\n'）
    #zip将两个列表 new_title 和 new_body 中的元素一一对应起来，返回一个迭代器，其中每个元素都是一个包含对应位置元素的元组。
    #print(new_title)
    #print(new_body)
    print(f'"完成打印"{chapter_url}') #查看打印到哪里了
    with open('HongLouMeng.txt','a',encoding='utf-8') as file:  #'a' attend 新元素添加到后面
        for all_content in all_contents:
            file.writelines(all_content)
