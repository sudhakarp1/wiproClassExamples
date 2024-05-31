import  pymysql

conn =pymysql.connect(host ="localhost", user= "root", password = "", database = 'playerdb')

cursor = conn.cursor()
FL = open("query.txt", "r")

for query in FL.readlines():
    print(query)
    cursor.execute(query)

conn.commit()
FL.close()
conn.close()