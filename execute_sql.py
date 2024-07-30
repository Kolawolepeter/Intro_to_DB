import mysql.connector

def execute_script_from_file(filename):
    with open(filename, 'r') as file:
        script = file.read()
    return script

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    cursor = conn.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    cursor.execute("USE alx_book_store")

    # Execute the SQL script
    script = execute_script_from_file('task_2.sql')
    for result in cursor.execute(script, multi=True):
        pass  # Iterate through each statement in the script
    print("Tables created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
