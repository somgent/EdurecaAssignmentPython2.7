# Sqlite3 Database Version

import sqlite3
con = sqlite3.connect("test.db")
with con:
    cur = con.cursor()
    data = cur.execute("SELECT sqlite_version();").fetchone()
    print "SQLite version: %s" % data