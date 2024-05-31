import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='myExample')

mycursor = mydb.cursor()
#mycursor.execute('CREATE TABLE demo (name VARCHAR(30), age INTEGER)')
mycursor.execute('SHOW TABLES')

for var in mycursor:
    print(var)

