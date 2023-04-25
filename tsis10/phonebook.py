import psycopg2
import csv

# Connect to Database
conn = psycopg2.connect("dbname=phonebook user=postgres password=Ao511792")
cur = conn.cursor()

# Create tables
# cur.execute("CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), phone VARCHAR(15));")

# Insert data from CSV
with open('users.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        cur.execute("INSERT INTO users (username, first_name, last_name, phone) VALUES (%s, %s, %s, %s);", row)
conn.commit()

# Insert from console
# username = input("Enter username: ")
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# phone = input("Enter phone: ")
# cur.execute("INSERT INTO users (username, first_name, last_name, phone) VALUES (%s, %s, %s, %s);", (username, first_name, last_name, phone))
# conn.commit()

# Update
username = input("Enter username to update: ")
phone = input("Enter new phone: ")
cur.execute("UPDATE users SET phone=%s WHERE username=%s;", (phone, username))
conn.commit()

# Query
cur.execute("SELECT * FROM users;")
for row in cur:
    print(row)

# Delete
username = input("Enter username to delete: ")
cur.execute("DELETE FROM users WHERE username=%s;", (username,))
conn.commit()

# Close connection
cur.close()
conn.close()