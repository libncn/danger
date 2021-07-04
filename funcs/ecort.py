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
from . import config

# 获取场地不陪同数据
def getdata(date1, date2):
    try:
        # SQL字符串模板渲染，添加查询条件
        sql = config.ecortSQL.format(startDate=date1, endDate=date2)

        # 打开数据库连接，查询数据获取数据列表rows
        IP = config.IP
        USR = config.USR
        PWD = config.PWD
        DB = config.DB
        SITE = config.SITE
        conn = pymssql.connect(IP, USR, PWD, DB)
        curs = conn.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()
        conn.close()

        lis = list()
        k = 0
        for tup in rows:
            k = k + 1
            dic = {'id':k, 'deptname':SITE[tup[0]], 'sitename':tup[0], 'num1':tup[1], 'num2':tup[2], 'dc1':('否' if tup[1]==0 or tup[2]==0 else '是'), 'dc2':('否' if tup[1]==0 and tup[2]==0 else '是')}
            lis.append(dic)
        dic = {'code': 0, 'msg': '', 'count': len(lis), 'data':lis}
        return dic

    except Exception as err:
        dic = {
            'code': 0,
            'msg': '',
            'count': 0,
            'data': []
        }
        return dic

# 获取分类汇总数据
def getdata2(date1, date2):
    try:
        # SQL字符串模板渲染，添加查询条件
        sql = config.ecortSQL2.format(startDate=date1, endDate=date2)

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
        return dic

    except Exception as err:
        dic = {
            'code': 0,
            'msg': '',
            'count': 0,
            'data': []
        }
        return dic
