from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import pymysql.cursors


import urlparser

# 请求URL并把结果用UTF-8编码
resq = urlopen("https://www.pk.cn/portal-glossary").read().decode("utf-8")


# 使用BeautifulSoup去解析
soup = bs(resq, "html.parser")


# 获取所有以/glossary/开头的a标签的href属性
listUrl = soup.findAll("a", href=re.compile("^/portal"))
# listUrls = re.compile('a href=(.*?)')
print(listUrl)
# 输出所有词条对应的名称和url
for url in listUrl:
    # print(url.get_text())
    url = "https://www.pk.cn%s" % url
    print(url)
    # print(url.get_text(), "<----------->", mainpage + url['href'])
    # urls = mainpage + url['href']
    # ur = urlopen(url=urls, timeout=1)
    # print(ur)
    # print(ur)

    # 过滤以。。。的URL，逗号要以反斜杠进行转义
    # if not re.search("",url["href"]):
    # 输出URL的文字和对应的链接
    # print(url.get_text(), "<----->", "https://www.pk.cn" + url["href"])
    # urlSnd = "https://www.pk.cn" + url
    #
    # urlSnd = urlopen(urlSnd)
    # soup = bs(urlSnd, "html.parser")
    # tag = soup.findAll('div', class_='glossarySection--content')
    # print(tag.get_text())

    # config = {
    #     'host': '127.0.0.1',
    #     'port': 3306,
    #     'user': 'root',
    #     'password': '999324',
    #     'db': 'pokerlist',
    #     'charset': 'utf8mb4',
    #     'cursorclass': pymysql.cursors.DictCursor,
    # }
    #
    # # 连接到数据库
    # connection = pymysql.connect(**config)
    # try:
    #     # 获取会话指针
    #     with connection.cursor() as cursor:
    #         # 创建sql语句
    #         sql = "insert into`urls`(`urlname`,`urlhref`)values(%s,%s)"
    #
    #         # 执行sql语句
    #         cursor.execute(sql, (url.get_text(), "http://thepokerlogic.com" + url["href"]))
    #
    #         # 提交
    #         connection.commit()
    # finally:
    #     connection.close()

    