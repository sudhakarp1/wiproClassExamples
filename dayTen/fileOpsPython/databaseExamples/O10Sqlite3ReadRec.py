
import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect("playerdb.sqlite3")

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

plyTbl = from_db_cursor(cursor)
plyTbl.align['plyname'] = "l"
plyTbl.align['sport'] = "l"
plyTbl.align['acheivement'] = "l"

# cursor.fetchall()
# for row in cursor.fetchall():
#     print(row)

conn.close()

print(plyTbl)

