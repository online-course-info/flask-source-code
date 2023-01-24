from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return '<title>First Form App in Flask</title><h1 style="color:red;position:absolute;font-family:Ubuntu;left:45%;">Login Forum</h1><br><br><input type="text" placeholder="username or email" required><br><br><input type="password" placeholder="password" required><br><br><button style="width:6cm;height:0.8cm;background-color:rgb(255,87,107);color:white;border:none;position:absolute;">Login</button><br><b'