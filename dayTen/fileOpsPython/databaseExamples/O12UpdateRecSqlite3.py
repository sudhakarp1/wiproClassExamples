


import sqlite3
conn = sqlite3.connect("playersdb.sqlite3")

cursor = conn.cursor()
query = "update player set plyname = 'Pusarla Venkata Sindhu' where plyid = 'PLY510'"

cursor.execute(query)

conn.commit()
conn.close()