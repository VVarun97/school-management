import os
import pymysql
from pymysql.err import MySQLError

# Put your Aiven password in an environment variable instead of hardcoding it
# Windows (PowerShell):  $env:DB_PASSWORD="your_password"
# macOS/Linux:           export DB_PASSWORD="your_password"

HOST = "mysql-13-varunvaidya13-3628.c.aivencloud.com"
PORT = 24951
USER = "avnadmin"
PASSWORD = "AVNS_9HvoJlFA75MEA67V0Uh"

if not PASSWORD:
    raise ValueError("DB_PASSWORD environment variable is not set.")

timeout = 10


def connect(db_name="defaultdb"):
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=db_name,
        port=PORT,
        charset="utf8mb4",
        connect_timeout=timeout,
        read_timeout=timeout,
        write_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False,
    )


def main():
    connection = None

    try:
        # First connect to defaultdb
        connection = connect("defaultdb")
        cursor = connection.cursor()

        # Aiven may restrict CREATE DATABASE, so this is attempted safely
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS school_management")
            connection.commit()
            print("Database check complete.")
        except MySQLError as e:
            print(f"CREATE DATABASE skipped/failed on Aiven: {e}")

        # Create the table in the current database
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schools (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                latitude FLOAT NOT NULL,
                longitude FLOAT NOT NULL
            )
        """)
        connection.commit()
        print("Table 'schools' is ready.")

        # Insert sample data
        cursor.execute("""
            INSERT INTO schools (name, address, latitude, longitude)
            VALUES (%s, %s, %s, %s)
        """, ("ABC School", "Andheri, Mumbai", 19.0760, 72.8777))
        connection.commit()
        print("Sample row inserted.")

        # Fetch and display rows
        cursor.execute("SELECT * FROM schools")
        rows = cursor.fetchall()
        print("Current rows:")
        print(rows)

    except MySQLError as e:
        print(f"MySQL error: {e}")

    finally:
        if connection:
            connection.close()
            print("Connection closed.")


if __name__ == "__main__":
    main()