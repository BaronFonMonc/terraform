import MySQLdb
from flask import Flask

app = Flask(__name__)

#conn = MySQLdb.connect(
#      host="rc1b-8xtt6v6j6v24qm6v.mdb.yandexcloud.net",
#      port=3306,
#      db="db1",
#      user="user1",
#      passwd="user1user1",
#      ssl={'ca': '~/.mysql/root.crt'})

@app.route('/')
def hello_world():
    return "<h1>Hello, World!!!!<h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0')