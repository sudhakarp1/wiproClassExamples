

import sqlite3

conn = sqlite3.connect("playerdb.sqlite3")

cursor = conn.cursor()

query = "update player set acheivement = '150 Knock Outs' where plyid = 'PL001'"

cursor.execute(query)

conn.commit()

conn.close()


