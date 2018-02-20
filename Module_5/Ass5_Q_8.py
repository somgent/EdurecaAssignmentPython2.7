
#=============Update Values============

import sqlite3 as lite

uId = 1
uPrice = 62300
con = lite.connect('todo.db')
with con:
    cur = con.cursor()
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (415678, 6))
    con.commit()
    print "Number of rows updated: %d" % cur.rowcount