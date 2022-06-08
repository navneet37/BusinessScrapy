import sqlite3

conn = sqlite3.connect("business.db")
cur = conn.cursor()

def select_all():
    return cur.execute("select * from business")


all_ = select_all()
for biz in all_:
    print(biz)
