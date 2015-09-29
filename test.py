#coding:utf-8 
'''
Created on 2015年2月2日
@author: MQ
'''
import  urllib
import re
from urllib import urlretrieve


#获取指定url的html文本
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#获取符合匹配条件的url列表
def getUrlList(pattern,html):
    url_list = re.findall(pattern,html )
    return url_list

#保存指定url下的所有图片
def saveImage(url):
    pic_count = 0
    html = getHtml(url)
    pattern = r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>"""
    url_list = getUrlList(pattern, html)
    #print url_list
    for i in url_list:
        prefix = i[0:7:1]
        suffix = i[len(i)-4:len(i):1]
#         print prefix
        if (prefix == "http://" )and (suffix==".jpg" or suffix==".png" or suffix == ".gif"):
            urlretrieve(i,"e://pictures/"+str(pic_count)+suffix)
            pic_count = pic_count+1

def main():
    start_url = "http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html"
    saveImage(start_url)

if __name__ == '__main__':
    main()