import MySQLdb

conn = MySQLdb.connect(
      host="rc1b-8xtt6v6j6v24qm6v.mdb.yandexcloud.net",
      port=3306,
      db="db1",
      user="user1",
      passwd="user1user1",
      ssl={'ca': '~/.mysql/root.crt'})

cur = conn.cursor()
cur.execute('SELECT version()')

print(cur.fetchone()[0])

<<<<<<< HEAD
print("Hello, world!")

conn.close()
=======
conn.close()
>>>>>>> 237a99514a9a1401a0c9b57448a1a7e340fbe601
