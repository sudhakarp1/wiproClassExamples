
import sqlite3

conn = sqlite3.connect("playersdb.sqlite3")

cursor = conn.cursor()

conn.close()
