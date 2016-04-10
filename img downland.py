import urllib.request  # python3的urllib中的下载，打开函数引用需引入urllib.request


def getimg(url):  # 定义了一个函数
    # url = str(url)   本有此行，但发现input直接转换为字符串，便将此行注释掉
    a = 1  # 因发现大多数网站图片的后缀为 数字+.jpg ，所以如此
    while (a < 30):
        n = str(a)  # 此行将数字转换为字符串，方便下行进行url拼接
        imgurl = url + n + ".jpg"
        urllib.request.urlretrieve(imgurl, "%s.jpg" % a)
        print("成功下载%d.jpg" % a)
        a += 1


a = input("请输入url:")


getimg(a)
