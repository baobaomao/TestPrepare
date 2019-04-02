import dao

if __name__ == "__main__":
    # 连接数据库
    dbName = 'sit'
    dao = dao.Dao(dbName)
    conn = dao.conn
    cur = dao.cur

    #使用cursor进行各种操作
    sql_demo = "select riskcode from lcpol where contno = '201837070210006549'"
    x = cur.execute(sql_demo)
    print (x.fetchall())
    print (x.fetchone())

    dao.close()