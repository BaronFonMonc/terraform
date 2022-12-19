import MySQLdb
from flask import Flask

app = Flask(__name__)


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

conn.close()

@app.route('/')
def hello():
    cur = conn.cursor()
    cur.execute('SELECT version()')

    s = cur.fetchone()[0]

    conn.close()
    return s

app.run(host="0.0.0.0")