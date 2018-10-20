import pymysql.cursors


class ConnectDatabase:

    def pokerlist(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '999324',
            'db': 'pokerlist',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
        }
    # 连接到数据库
        connection = pymysql.connect(**config)
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql = "insert into`urls`(`urlname`,`urlhref`)values(%s,%s)"

                # 执行sql语句
                cursor.execute(sql, (url.get_text(), "http://thepokerlogic.com" + url["href"]))

                # 提交
                connection.commit()
        finally:
            connection.close()