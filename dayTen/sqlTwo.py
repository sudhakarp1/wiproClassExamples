import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')
print(conn)
# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM users')

# Get all the rows in the result set
users = cursor.fetchall()
    
# Close the connection to the database
conn.close()
# Print the users
for user in users:
    print(user)
