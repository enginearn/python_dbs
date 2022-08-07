#!/usr/bin/env python3

import sys
import mysql.connector
import configparser
import config

config = config.make_config()

host = config["MySQL"]["host_ip"]
port = config["MySQL"]["port"]
user = config["MySQL"]["user"]
password = config["MySQL"]["password"]


conn = mysql.connector.connect(host=host, port=port, user=user, password=password)
cursor = conn.cursor(buffered=True)
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

cursor.close()
conn.close()
if __name__ == '__main__':
    sys.exit(0)
