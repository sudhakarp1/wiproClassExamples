
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port=3306)

cursor = conn.cursor()

query = "create database playerDB"

cursor.execute(query)

conn.close()
