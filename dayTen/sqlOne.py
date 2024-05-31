import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)')


# Commit your changes to the database
conn.commit()

cursor.execute("""
    INSERT INTO users VALUES
        ('Monty Python', 75),
        ('Completely Different', 71)
    """)
conn.commit()
# Close the connection to the database
conn.close()