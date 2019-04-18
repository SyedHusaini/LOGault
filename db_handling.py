#!/usr/bin/python
#
# from sqlalchemy import create_engine
# # Connect to the database
# '''creates an SQLAlchemy engine for database connection (was necessary to change for pandas dataframes )->(Asim_Sansi)'''
# engine = create_engine('mysql+pymysql://root:tipu@localhost:3306/logault_final')
# '''binds the engine with an object which we'll use to execute SQl scripts and so on...->(Asim_Sansi)'''
# connection = engine.connect()






import pymysql
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='tipu',
                             db='logault_final',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

