#!/usr/bin/python

import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='tipu',
                             db='logault_database',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        a = ["hello", 2 ,4, 8.4353, True, 'a']
        print (a)

        sql = "SELECT `*` FROM `referance`"
        cursor.execute(sql)
        result = cursor.fetchone()
        for i in result:
           print(i)
finally:
    connection.close()

