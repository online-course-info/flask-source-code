from flask import Flask
from passlib.hash import sha256_crypt
import mysql.connector as mariadb

app = Flask(__name__)
mariadb_connection = mariadb.connect(user='chooseAUserName', password='choosePassword',database='Login')

@app.route('/')

def index():
    username = 'newUserName'
    password = sha256_crypt.encrypt("newPassword")
    email = "what@ever.com"

    cur = mariadb_connection.cursor()
    cur.execute('INSERT INTO Login (username, password, email) VALUES ( %s %s %s )', ( username, password, email ) )
    mariadb_connection.commit()
    cur.close()

    return ''


if __name__ == "__main__":
    app.run(debug= True,host= '0.0.0.0',port= '5000')