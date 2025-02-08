from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sq
import os
# import matplotlib.pyplot as plt

app = Flask(__name__)
DBPATH="data/database.db"

@app.route('/')
def home():
    return render_template('index.html',server_msg='')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/login_account',methods=['POST','GET'])
def login_account():
    username = request.form.get('username', None)
    password = request.form.get('pass', None)
    t=get_user(username,password)
    if((username=='' or password=='')or len(t)==0):
        return render_template('index.html',server_msg='invalid username or password')
    else:
        return render_template('time.html',server_msg=f'welcome {username}')


@app.route('/create_account',methods=['POST','GET'])
def create_account():
    username = request.form.get('username', None)
    password = request.form.get('pass', None)
    if(username=='' or password==''):
        return render_template('index.html',server_msg='ya 7mar da5l bl s7i7')
    else:
        t=get_username(username)
        if len(t)!=0:
            return render_template('index.html',server_msg='username already existe')
        else:
            insert_user(username,password)
            return render_template('index.html',server_msg=f'welcome {username} , account created successfully')

def create_tables():
    conn = sq.connect(DBPATH)
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users
                (username text PRIMARY KEY, password text)
                ''')
    conn.commit()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users_times
                (username text PRIMARY KEY,
                day text,
                time DATETIME,
                matier text,
                FOREIGN KEY (username) REFERENCES users (username))
                ''')
    conn.commit()
    conn.close()


def get_user(user,password):
    conn = sq.connect(DBPATH)
    cur = conn.cursor()
    res = cur.execute("SELECT username FROM users WHERE username = ? AND password = ?",(user,password))
    t=res.fetchall()
    conn.commit()
    conn.close()
    return t 


def get_username(user):
    conn = sq.connect(DBPATH)
    cur = conn.cursor()
    res = cur.execute("SELECT username FROM users WHERE username = ?",(user,))
    t=res.fetchall()
    conn.commit()
    conn.close()
    return t 


def insert_user(user,password):
    conn = sq.connect(DBPATH)
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO users VALUES(?,?)
                ''',(user,password,))
    conn.commit()
    conn.close()



@app.route('/create_new_timeline')
def new_time():
    return render_template('create_new_timeline.html')


@app.route('/create_new_timeline',methods=['POST','GET'])
def create_newT():
    day = request.form.get('day', None)
    startT = request.form.get('stime', None)
    endT = request.form.get('etime', None)
    print(day)
    if (day=="0" or day=="7"):
        return render_template('create_new_timeline.html',server_msg="choose the right day")  
    return render_template('create_new_timeline.html',server_msg="..")


@app.route('/edit_time')
def editT():
    return render_template('edit_time.html',server_msg="")



@app.route('/user_time')
def userT():
    return render_template('user_time_table.html',server_msg="")










def main():
    create_tables()
    app.run(debug=True)


if __name__=="__main__":
    main()