import cx_Oracle

# 用户名/密码@IP:端口号/SERVICE_NAME
class DbInfo(object):
    def get_dbInfo(self,dbName):
        if dbName.lower() == 'sit':
            self.username = 'lis7sit'
            self.password = 'lis7sit'
            self.ip = '10.0.56.125:1521'
            self.service_name = 'lis7test'
        elif dbName.lower() == 'uat':
            self.username = 'lis7uat'
            self.password = 'lis7uat'
            self.ip = '10.0.56.125:1521'
            self.service_name = 'lis7test'
        return self.username + "/" + self.password + "@" + self.ip + "/" + self.service_name

class Dao(object):
    def __init__(self,dbName):
        self.dbName = dbName
        dbInfo = DbInfo().get_dbInfo(dbName)
        self.conn = cx_Oracle.connect(dbInfo)
        # 获取cursor
        self.cur = self.conn.cursor()
        print("连接至数据库：" + dbName)
    def close(self):
        self.cur.close()
        self.conn.close()
        print("断开数据库：" + self.dbName)

