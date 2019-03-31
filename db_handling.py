#!/usr/bin/python

import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='tipu',
                             db='logault_final',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

