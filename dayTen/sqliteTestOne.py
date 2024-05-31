import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT * from users')
users = cursor.fetchall()

conn.close()

for user in users:
    print(user)
'''
    connecting to database 
        With in one database we can any number of tables 
            within each table we can any number of records
                each record has number of fields

    C --> creating  records
    R --> Reading from the table  
    U --> updating the existing records 
    D --> deleting records
'''

