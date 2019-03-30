#!/usr/bin/python

import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='testing',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `*` FROM `label`"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
           print(i["tag_name"])
finally:
    connection.close()

