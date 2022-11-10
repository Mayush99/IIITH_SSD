import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
login = False


@app.route('/user/signup',methods = ['POST'])
def register():
    con = sqlite3.connect('users.db')
    c = con.cursor()
    if(request.form["name"]!="" and request.form["email"]!="" and request.form["password"]!=""):
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        stmt = f"Selct * from user WHERE name='{name}' and password='{password}';"
        c.execute(stmt)
        data = c.fetchone()
        if not data:
            c.execute("INSERT INTO user (name,email,password) values (?,?,?)",(name,email,password))
            con.commit()
            con.close()
            return redirect(url_for('login'))

@app.route('/user/signin',methods=['POST'])
def login():
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    email = request.form['email']
    password = request.form['password']
    con = sqlite3.connect('users.db')
    c = con.cursor()
    stmt = f"SELECT * from user WHERE email='{email}' and password='{password}';"
    result = c.execute(stmt)
    print(result.fetchall())


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/')
def index():
    login = False
    if 'username' in session:
        login = True
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.secret_key = 'asdsdfsdfs13sdf_df%&'
    con = sqlite3.connect('users.db')
    c = con.cursor
    c.execute(
        "CREATE TABLE IF NOT EXISTS user(name text, email text, password text);")
    con.commit()
    app.run(debug=True)