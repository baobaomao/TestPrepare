import cx_Oracle                                          #引用模块cx_Oracle
conn=cx_Oracle.connect('lis7sit/lis7sit@10.0.56.125:1521/lis7test')    #连接数据库 用户名/密码@IP:端口号/SERVICE_NAME
c=conn.cursor()                                           #获取cursor
x=c.execute("select riskcode from lcpol where contno = '201837070210006549'")                   #使用cursor进行各种操作
print (x.fetchone())
c.close()                                                 #关闭cursor
conn.close()                                              #关闭连接