# -*- coding:utf-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
import pymysql

# mysql连接信息（字典形式）
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'JDProducts',
    'charset': 'utf8'
}
# 获得数据库连接
connection = pymysql.connect(**db_config)

url = r'https://www.joybuy.com/search?keywords=toy&arriveCountry=2456&showType=grid&pageSize=48&page='

bashurl = r'&filterTypes=expand'
# 模拟浏览器头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
try:
    for i in range(1, 64):
        print ("---------------parse the " + str(i) + " page---------------")
        res = requests.get(url + str(i) + bashurl, headers=headers)
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        goods = soup.find_all('div', class_="g-item")

        # 获得数据库游标
        with connection.cursor() as cursor:
            sql = 'insert into JD( img_url,title) values(%s, %s)'
            for good in goods:
                title = good.find(class_="p-title").find('a').string.replace('\t', '').replace('\n', '')
                img_url = good.find(class_="p-img").find('img')['src']

                # 执行sql语句
                cursor.execute(sql, (img_url, title))
        # 事务提交
        connection.commit()
finally:
    # 关闭数据库连接
    connection.close()
