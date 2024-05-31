

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="playerdb")

cursor = conn.cursor()

query = "update player set plyname = 'Sachin Ramesh Tendulkar' where plyid = 'PL020'"

cursor.execute(query)

conn.commit()

conn.close()

