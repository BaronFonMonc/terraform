import MySQLdb


conn = MySQLdb.connect(
      host="rc1b-8xtt6v6j6v24qm6v.mdb.yandexcloud.net",
      port=3306,
      db="db1",
      user="user1",
      passwd="user1user1",
      ssl={'ca': '~/.mysql/root.crt'})

cur = conn.cursor()
cur.execute('CREATE TABLE CLIENT ( ID INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT );')
cur.execute('')

print("Current version is:" + cur.fetchone()[0])

conn.close()