
import sqlite3
from unicodedata import name
from flask import Flask, flash, redirect,render_template, session,url_for,request
app = Flask(__name__)
con = sqlite3.connect('details.db')
cursor = con.cursor()
con.execute("create table if not exists userDetail(pid  INTEGER PRIMARY KEY ,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password TEXT)")
print('table created')
con.close()
app.secret_key = '123'

@app.route('/')#it takes / as invoking function call invoke call
def login():
    return render_template('home.html')     


@app.route('/regPage', methods=['POST'])
def regPage():
    msg=''
    try:
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        con = sqlite3.connect('details.db')

        print("table connected")
        cursor = con.cursor()
        cursor.execute("INSERT INTO  userDetail(name,email,password) VALUES (?,?,?)",(name, email, password) )
        con.commit()
        con.close()
        msg = "Record successfully added"
    except sqlite3.Error as error :
        con.rollback()
        msg = "error in insert operation",error
        print(msg)
    finally:
        return "Registered Successfully login Mr."+name
        con.close()

@app.route('/loginPage1',methods=['GET', 'POST'])
def loginPage1():
    
    msg=''
    print(request)
    name = request.form['username']
    password = request.form['password']
    con = sqlite3.connect('details.db')
    print("vaidate start")
    # con.row_factory=sqlite3.Row
    cursor = con.cursor()
    cursor.execute("select * from userDetail where name=?  and password=?",(name,password))
    data = cursor.fetchone()
    if data:
        session["name"]=data[0]#here we used session to store the datas of data[name,password]
       # session["password"]=data[1]
        print(data[0])
        return "login success"
    else:
        return "login failed"
        



    

@app.route('/register') #method1 to move from page to page in href call the method name known as regPage eg: href={{erl_for('regpage)}}
def register():
    return render_template('register.html')





if __name__ == '__main__': #it will consider main as main function
    app.run(debug=True,port=5600)#telling app file to run,address already mea