# this file is the database connector
# You should have installed the mysql library

import mysql.connector as connector

config = {
    'user': 'test',
    'password': 'test',
    'host': 'localhost',
    'port': 8809,
    'database': 'python'
}

db = connector.connect(**config)
cursor = db.cursor()
