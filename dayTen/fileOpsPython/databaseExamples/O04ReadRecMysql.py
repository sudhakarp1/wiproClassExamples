
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="playerdb")

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

plytbl = from_db_cursor(cursor)

print(plytbl)

conn.close()

#
#
# for rec in cursor.fetchall():
#     print(rec)
#
# conn.close()