from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import pymysql.cursors
from urllib.parse import urljoin


# 请求URL并把结果用UTF-8编码
resq = urlopen("https://www.pk.cn/portal-glossary-gkeyword-id-fd4b373047e89411188f56472eab267c.html").read().decode("utf-8")


# 使用BeautifulSoup去解析
soup = bs(resq, "html.parser")


# 获取所有以/glossary/开头的a标签的href属性
listUrls = soup.findAll('div', class_='glossarySection--content')


# 输出所有词条对应的名称和url
for url in listUrls:
    # 过滤以。。。的URL，逗号要以反斜杠进行转义
    # if not re.search("",url["href"]):
    # 输出URL的文字和对应的链接

    print(url.get_text())
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
    #         sql = "insert into`test`(`urlname`,`urlhref`)values(%s,%s)"
    #
    #         # 执行sql语句
    #         cursor.execute(sql, (url.get_text(), "https://www.pk.cn" + url["href"]))
    #
    #         # 提交
    #         connection.commit()
    # finally:
    #     connection.close()

