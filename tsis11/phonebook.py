import psycopg2
import csv

# Connect to Database
conn = psycopg2.connect("dbname=phonebook user=postgres password=Ao511792")
cur = conn.cursor()

# Create tables (if not exists)
cur.execute("""CREATE TABLE IF NOT EXISTS users (
                   user_id SERIAL PRIMARY KEY,
                   username VARCHAR(50),
                   first_name VARCHAR(50),
                   last_name VARCHAR(50),
                   phone VARCHAR(15)
               );""")
conn.commit()

# Create functions and stored procedures
sql_functions = '''
-- Other DROP and CREATE statements...

DROP FUNCTION IF EXISTS search_users(TEXT);

CREATE OR REPLACE FUNCTION search_users(pattern TEXT)
RETURNS TABLE(user_id IN            T, username VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), phone VARCHAR(50)) AS $$
BEGIN
  RETURN QUERY SELECT u.* FROM users u WHERE
    u.username ILIKE '%' || pattern || '%' OR
    u.first_name ILIKE '%' || pattern || '%' OR
    u.last_name ILIKE '%' || pattern || '%' OR
    u.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Procedure to insert or update user
CREATE OR REPLACE PROCEDURE upsert_user(p_username TEXT, p_first_name TEXT, p_last_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM users WHERE username = p_username) THEN
    UPDATE users SET phone = p_phone WHERE username = p_username;
  ELSE
    INSERT INTO users (username, first_name, last_name, phone) VALUES (p_username, p_first_name, p_last_name, p_phone);
  END IF;
END;
$$;

-- Type and procedure for inserting multiple users
DROP TYPE IF EXISTS user_data CASCADE;

CREATE TYPE user_data AS (username TEXT, phone TEXT);

CREATE OR REPLACE FUNCTION insert_users(p_users user_data[]) RETURNS VOID
LANGUAGE plpgsql
AS $$
DECLARE
  user_element user_data;
  incorrect_data user_data[] := ARRAY[]::user_data[];
BEGIN
  FOREACH user_element IN ARRAY p_users
  LOOP
    IF LENGTH(user_element.phone) = 10 THEN -- Adjust the condition as per your requirements
      CALL upsert_user(user_element.username, NULL, NULL, user_element.phone);
    ELSE
      incorrect_data := incorrect_data || user_element;
    END IF;
  END LOOP;

  IF array_length(incorrect_data, 1) > 0 THEN
    RAISE NOTICE 'Incorrect data: %', incorrect_data;
  END IF;
END;
$$;

DROP FUNCTION IF EXISTS get_users_paginated(INTEGER, INTEGER);

-- Function for pagination
CREATE OR REPLACE FUNCTION get_users_paginated("limit" INT, "offset" INT)
RETURNS TABLE(user_id INT, username VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), phone VARCHAR(50)) AS $$
BEGIN
  RETURN QUERY SELECT * FROM users ORDER BY user_id LIMIT "limit" OFFSET "offset";
END;
$$ LANGUAGE plpgsql;

-- Procedure to delete user by username or phone
CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
  DELETE FROM users WHERE username = p_username OR phone = p_phone;
END;
$$;
'''

cur.execute(sql_functions)
conn.commit()

# Search users
pattern = input("Enter search pattern: ")
cur.callproc("search_users", [pattern])
print("Search results:")
for row in cur.fetchall():
    print(row)

# Insert or update user
username = input("Enter username: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone: ")
cur.execute("CALL upsert_user(%s, %s, %s, %s)", (username, first_name, last_name, phone))
conn.commit()

# Insert multiple users
users = [
    ('user1', '1111111111'),
    ('user2', '2222222222'),
    ('user3', '3333333333')
]
cur.execute("SELECT insert_users(%s::user_data[])", (users,))
conn.commit()

# Get users with pagination
limit = 5
offset = 0
cur.callproc("get_users_paginated", [limit, offset])
print("Users with pagination:")
for row in cur.fetchall():
    print(row)

# Delete user by username or phone
username = input("Enter username to delete: ")
phone = input("Enter phone to delete: ")
cur.execute("CALL delete_user_by_username_or_phone(%s, %s)", (username, phone))
conn.commit()

# Close connection
cur.close()
conn.close()