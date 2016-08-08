import requests
from bs4 import BeautifulSoup
import re
from urllib import request

def gethtml(url):
    HEADERS = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'AIDUID=EB3E97CCCCC70480B959301E9AD16905:FG=1; locale=zh; BIDUPSID=EB3E97CCCCC70480B959301E9AD16905; PSTM=1464408270; H_PS_PSSID=18881_20141_1446_19570_17001_15285_11536',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'DNT':'1'

    }
    html = requests.get(url, headers=HEADERS)
    word = html.text
    #print(word)
    soup = BeautifulSoup(word)
    s = soup.find_all('img')
    #print(s)
    for i in s:
        z = i.get('src')
        if re.findall('imgsrc.baidu.com',z):
            img = request.urlopen(z)
            imgr = img.read()
            try:
                file = open(z[-7:],'wb')
                file.write(imgr)
                file.close()
                print('保存图片'+z)
            except IOError:
                print("IOError")





url = input("请输入贴吧网址: ")
gethtml(url)
'''
Accept:*/*
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Cookie:BAIDUID=EB3E97CCCCC70480B959301E9AD16905:FG=1; locale=zh; BIDUPSID=EB3E97CCCCC70480B959301E9AD16905; PSTM=1464408270; H_PS_PSSID=18881_20141_1446_19570_17001_15285_11536

#post_content_90321290196 > img
#j_p_postlist > div:nth-child(1) > div.d_post_content_main.d_post_content_firstfloor > div.thread_recommend.thread-recommend > div.thread_list_slideshow > ul > div:nth-child(1) > li:nth-child(1) > a
'''
