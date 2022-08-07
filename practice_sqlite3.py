#!/usr/bin/env python3

import sys
import sqlite3
import datetime

now = datetime.datetime.now().isoformat(sep=' ')
# conn = sqlite3.connect("./sqlite/test_sqlite3.db")
conn = sqlite3.connect(":memory:")
curs = conn.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, data TEXT, name TEXT)")
curs.execute("INSERT INTO persons (data, name) VALUES (?, ?)", (now, "John Smith"))
curs.execute("INSERT INTO persons (data, name) VALUES (?, ?)", (now, "Mary Jane"))

curs.execute("SELECT * FROM persons")
print(curs.fetchall())
curs.execute("UPDATE persons SET name = 'John Doe' WHERE name = 'John Smith'")
conn.commit()

curs.execute("DELETE FROM persons WHERE name = 'Mary Jane'")
curs.execute("UPDATE persons SET name = 'John Smith' WHERE name = 'John Doe'")
curs.execute("SELECT * FROM persons")
conn.commit()
print(curs.fetchall())

curs.close()
conn.close()

if __name__ == '__main__':
    sys.exit(0)

