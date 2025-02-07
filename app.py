from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sq
import os
# import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html',server_msg='')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_account',methods=['POST','GET'])
def create_account():
    username = request.form.get('username', None)
    password = request.form.get('pass', None)
    if(username=='' or password==''):
        return render_template('index.html',server_msg='ya 7mar da5l bl s7i7')
    else:

        return render_template('index.html',server_msg='')

def create_tables():
    conn = sq.connect('database.db')
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users
                (username text PRIMARY KEY, password text)
                ''')
    conn.commit()
    conn.close()


def insert_user():
    conn = sq.connect('users.db')
    cur = conn.cursor()



def main():
    app.run(debug=True)


if __name__=="__main__":
    main()