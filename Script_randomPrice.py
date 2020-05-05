import pymysql
import random


conn = pymysql.connect(host='localhost', user='root', password='root', db='testdb')
cmd = 'SELECT name FROM cards;'
cur = conn.cursor()
cur.execute(cmd)

names = cur.fetchall()

cmd = ''
cur = conn.cursor()
for x in names:
    cmd = 'INSERT INTO Catalog(id, price) VALUES (\"' + x[0] + '\", ' + str(random.randrange(1, 500)) + ');'
    cur.execute(cmd)

conn.commit()
conn.close()