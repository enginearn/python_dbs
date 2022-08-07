#!/usr/bin/env python3

import os
import sqlite3
import sys

import psycopg
import pymongo
from dotenv import load_dotenv
from MySQLdb import _mysql as mysql

load_dotenv(".env")


def mysql_connect():
    MYSQL_HOST = os.getenv("mysql_host")
    MYSQL_USER = os.getenv("mysql_user")
    MYSQL_PORT = os.getenv("mysql_port")
    MYSQL_PASSWORD = os.getenv("mysql_password_local")

    try:
        mysql_cn = mysql.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            port=int(MYSQL_PORT),
        )
        print("Connected to MySQL!")
        mysql_cn.query("""SHOW DATABASES;""")
        for db in mysql_cn.store_result().fetch_row(0):
            print(db)
        return mysql_cn

    except mysql.Error as e:
        print(f"MySQL: {e}")
        return None

    finally:
        print("MySQL connection closed.")
        mysql_cn.close()


def mongo_connect():
    MONGO_HOST = os.getenv("mongo_host")
    MONGO_PORT = os.getenv("mongo_port")

    try:
        client = pymongo.MongoClient(MONGO_HOST, int(MONGO_PORT))
        print("Connected to MongoDB!")
        return client

    except pymongo.errors.ConnectionFailure as e:
        print(e)
        return None

    finally:
        print("MongoDB connection closed.")
        client.close()


def postgres_connect():
    PSQL_HOST = os.getenv("psql_host")
    PSQL_USER = os.getenv("psql_user")
    PSQL_PASSWORD = os.getenv("psql_password_local")
    PSQL_PORT = os.getenv("psql_port")

    try:
        psql_cn = psycopg.connect(
            f"user={PSQL_USER} password={PSQL_PASSWORD} port={PSQL_PORT} host={PSQL_HOST}"
        )
        print("Connected to PostgreSQL!")
        for db in psql_cn.cursor().execute("SELECT datname FROM pg_catalog.pg_database;"):
            print(db)
        return psql_cn

    except psycopg.Error as e:
        print(f"postgres: {e}")
        return None

    finally:
        print("PostgreSQL connection closed.")
        psql_cn.close()


def sqlite_connect():
    try:
        sqlite_cn = sqlite3.connect("./sqlite/test.db")
        print("Connected to SQLite!")
        return sqlite_cn

    except sqlite3.Error as e:
        print(f"SQLite: {e}")
        return None

    finally:
        print("SQLite connection closed.")
        sqlite_cn.close()


def main():
    mysql_connect()
    mongo_connect()
    postgres_connect()
    sqlite_connect()


if __name__ == "__main__":
    main()
    sys.exit(0)
