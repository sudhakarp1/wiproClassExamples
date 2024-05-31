

import sqlite3

conn = sqlite3.connect("playersdb.sqlite3")

cursor = conn.cursor()

FL = open("Playersdata.txt", "r")

for query in FL.readlines():
    cursor.execute(query)
FL.close()

conn.commit()
conn.close()
