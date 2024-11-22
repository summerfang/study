import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # e.g., "postgresql://user:password@localhost/dbname"

# Initialize connection pool
try:
    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1,
        20,
        DATABASE_URL
    )
    if connection_pool:
        print("Connection pool created successfully")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

def get_db_connection():
    try:
        connection = connection_pool.getconn()
        if connection:
            return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error getting connection from pool", error)

def release_db_connection(connection):
    try:
        connection_pool.putconn(connection)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error releasing connection back to pool", error)