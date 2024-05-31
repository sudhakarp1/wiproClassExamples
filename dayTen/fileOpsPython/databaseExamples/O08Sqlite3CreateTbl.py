
import sqlite3

conn = sqlite3.connect("playerdb.sqlite3")

cursor = conn.cursor()

query = """
create table player(
plyid varchar(5) PRIMARY KEY,
plyname varchar(50) not null,
sport varchar(50) not null,
acheivement varchar(50) not null
)
"""

cursor.execute(query)

conn.close()
