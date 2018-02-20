
## Fetch the coulmn names of the store table created

import sqlite3

def store_data():
    with sqlite3.connect("store.db") as con:
        cur = con.cursor()

    print "Fetching added data from db to verify....\n"
    col_names = [cn[1] for cn in cur.execute("PRAGMA table_info('Store');")]
    cur.execute('SELECT * FROM Store;')
    rows = cur.fetchall()
    header = "%-17s %-19s %-30s %-2s" % (col_names[0], col_names[1], col_names[2], col_names[3])
    print "-" * (len(header) + 20)
    print header
    print "-" * (len(header) + 20)


if __name__ == '__main__':
    store_data()