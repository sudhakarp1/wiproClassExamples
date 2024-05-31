


import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="playerdb")

cursor = conn.cursor()

query = "delete from player where plyid = 'PL421'"

cursor.execute(query)

conn.commit()

conn.close()

