#!/usr/bin/env python3

import sys

import psycopg
import pymongo
from MySQLdb import _mysql as mysql


def mysql_connect():
    try:
        mysql_cn = mysql.connect(user='root', password='secret',
                                    host='localhost', port=3306) # host='127.0.0.1'
        print("Connected to MySQL!")
        return mysql_cn

    except mysql.Error as e:
        print(f"MySQL: {e}")
        return None

def mongo_connect():
    try:
        client = pymongo.MongoClient("localhost", 27017)
        print("Connected to MongoDB!")
        return client

    except pymongo.errors.ConnectionFailure as e:
        print(e)
        return None

def postgres_connect():
    try:
        psql_cn = psycopg.connect("user=postgres password=mysecretpassword port=5432 host=localhost") # host=127.0.0.1
        print("Connected to PostgreSQL!")
        return psql_cn

    except psycopg.Error as e:
        print(f"postgres: {e}")
        return None

def main():
    mysql_connect()
    mongo_connect()
    postgres_connect()

if __name__ == '__main__':
    main()
    sys.exit(0)
