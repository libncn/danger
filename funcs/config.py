# -*- coding:utf-8 -*-

'''
   文件: config.py
   路径: D:\www\pyfunc\config.py
   时间: 2021/06/06 10:35:28
   作者: Li Bin（BBN）
   版本: 1.0
   说明: 配置文件
'''


        
# SQL字符串（不陪同查验统计）
ecortSQL = '''
        SELECT
            SITENAME as SITE,
            SUM(CASE WHEN ECORTMEMO='不陪同' THEN 1 ELSE 0 END) AS NOECORT,
            SUM(CASE WHEN ECORTMEMO='委托' THEN 1 ELSE 0 END) AS TDECORT
        FROM INSPDATA
        WHERE (PLANDATE BETWEEN '{startDate} 00:00:00' and '{endDate} 23:59:59')
            AND INSPMODE<>'机检'
        GROUP BY SITENAME
        ORDER BY
            CASE SITENAME
                WHEN '外港一期' THEN 1
                WHEN '外港二期' THEN 2
                WHEN '外港四期' THEN 3
                WHEN '外港五期' THEN 4
                WHEN '浦东物流' THEN 5
                WHEN '三骏仓库' THEN 6
                WHEN '上港外分' THEN 7
                WHEN '外五2号点' THEN 8
                WHEN '上港冷链7K' THEN 9
                WHEN '上港冷链' THEN 10
            END
        '''
