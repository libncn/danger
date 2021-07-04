# -*- coding:utf-8 -*-
'''
   文件: test.py
   路径: D:\www\pyfunc\ecort.py
   时间: 2021/06/06 10:36:45
   作者: Li Bin（BBN）
   版本: 1.0
   说明: 获取不陪同查验数据，参数（日期起止），返回（数据字典）
'''

import pymssql
import config


sql = config.ecortSQL2.format(startDate='2021-06-01', endDate='2021-06-22')

# 打开数据库连接，查询数据获取数据列表rows
IP = config.IP
USR = config.USR
PWD = config.PWD
DB = config.DB
conn = pymssql.connect(IP, USR, PWD, DB)
curs = conn.cursor()
curs.execute(sql)
row = curs.fetchone()
curs.close()
conn.close()
lis = [{'t':row[0], 't1':row[1], 't0':row[2], 't2':row[3], 'e':row[4], 'p':row[5], 'e1':row[6], 'p1':row[7], 'e0':row[8], 'p0':row[9], 'e2':row[10], 'p2':row[11]}]

dic = {'code': 0, 'msg': '', 'count': 1, 'data':lis}
print(dic)
