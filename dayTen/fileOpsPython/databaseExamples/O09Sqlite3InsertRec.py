
import sqlite3

conn = sqlite3.connect("playerdb.sqlite3")

cursor = conn.cursor()

FL = open("query.txt", "r")

for query in FL.readlines():
    print(query)
    cursor.execute(query)

conn.commit()

conn.close()
