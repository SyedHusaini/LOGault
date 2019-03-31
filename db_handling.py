#!/usr/bin/python

import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='logault',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

