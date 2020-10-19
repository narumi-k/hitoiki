import os
from flask import Flask , render_template , request , redirect , session
import sqlite3
from datetime import datetime
app = Flask(__name__)

app.secret_key = 'sunabaco'

@app.route('/',methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if 'user_id' in session :
            return redirect ('/aaa')
        else:
            return render_template("regist.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect('hitoiki.db')
        c = conn.cursor()
        c.execute("insert into user values(null,?,?)", (name,password))
        conn.commit()
        conn.close()
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'user_id' in session :
            return redirect("/aaa")
        else:
            return render_template("login.html")
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        conn = sqlite3.connect('hitoiki.db')
        c = conn.cursor()
        c.execute("select id from user where name = ? and password = ?", (name, password) )
        user_id = c.fetchone()
        conn.close()
        print(type(user_id))
        if user_id is None:
            return render_template("login.html")
        else:
            session['user_id'] = user_id[0]
            return redirect("/aaa")

@app.route("/aaa")
def pose():
    return render_template("question1.html")



@app.route('/one', methods=['POST'])
def out_one():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,1,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question2.html")



@app.route('/two', methods=['POST'])
def out_two():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,2,?,?)", (user_id ,name, time))
    conn.commit()
    conn.close()
    return render_template("question3.html")


@app.route('/three', methods=['POST'])
def out_three():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,3,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question4.html")


@app.route('/four', methods=['POST'])
def out_four():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,4,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question5.html")


@app.route('/five', methods=['POST'])
def out_five():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,5,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question6.html")


@app.route('/six', methods=['POST'])
def out_six():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,6,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question7.html")


@app.route('/seven', methods=['POST'])
def out_seven():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,7,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question8.html")


@app.route('/eight', methods=['POST'])
def out_eight():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,8,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question9.html")


@app.route('/nine', methods=['POST'])
def out_nine():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,9,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return render_template("question10.html")


@app.route('/ten', methods=['POST'])
def out_ten():
    user_id=session['user_id']
    name = int(request.form.get("radio"))
    print(name)
    time = datetime.now().strftime('%Y/%m/%d')
    conn = sqlite3.connect('hitoiki.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO question VALUES (null,?,10,?,?)", (user_id, name, time))
    conn.commit()
    conn.close()
    return redirect("/dbtest")


@app.route("/dbtest")
def dbtest():
    user_id=session['user_id']
    #flask.dbに接続
    conn = sqlite3.connect("hitoiki.db")
    #中身が見れるように
    c = conn.cursor()
    #SQL文を実行
    c.execute("select anser  from question where question_id = 1 order by id  desc")
    #取ってきたレコードを格納(user_infoに代入している)
    list1 = c.fetchall()
    print(list1)
    c.execute("select anser  from question where question_id = 2 order by id desc ")
    list2 = c.fetchall()
    print(list2)
    c.execute("select anser  from question where question_id = 3 order by id desc ")
    list3 = c.fetchall()
    c.execute("select anser  from question where question_id = 4 order by id desc ")
    list4 = c.fetchall()
    c.execute("select anser  from question where question_id = 5 order by id desc ")
    list5 = c.fetchall()
    c.execute("select anser  from question where question_id = 6 order by id desc ")
    list6 = c.fetchall()
    c.execute("select anser  from question where question_id = 7 order by id desc ")
    list7 = c.fetchall()
    c.execute("select anser  from question where question_id = 8 order by id desc ")
    list8 = c.fetchall()
    c.execute("select anser  from question where question_id = 9 order by id desc ")
    list9 = c.fetchall()
    c.execute("select anser  from question where question_id = 10 order by id desc ")
    list10 = c.fetchall()



    c.execute("select date  from question where question_id = 1 AND user_id = ? order by id desc",(user_id,))
    time = c.fetchall()
    print(time)
    # dbとの接続を切る
    c.close()
    # list1 = [(1,2), (1,3), (2,4)]
    return render_template("result.html",list1=list1, list2=list2, list3=list3 ,list4=list4, list5=list5, list6=list6, list7=list7, list8=list8,list9=list9, list10=list10, time=time)

@app.route("/logout")




def logout():

    session.pop('user_id',None)
    # ログアウト後はログインページにリダイレクトさせる
    return redirect("/")




if __name__ == "__main__":
    
    app.run(debug=True)