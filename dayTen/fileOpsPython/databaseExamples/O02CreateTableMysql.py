
import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="", database="playerDB")
cursor = conn.cursor()

query = """
create table player (
plyid varchar(5) PRIMARY KEY,
plyname varchar(50) not null,
sport varchar(50) not null,
achievement varchar(50) not null )
"""
cursor.execute(query)
conn.close()
