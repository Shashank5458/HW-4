from flask import Flask, render_template, request
import sqlite3
app=Flask(__name__)
 
@app.route('/')
def index():
   return render_template('home.html')

@app.route('/mainpy',methods = ['POST', 'GET'])
def mainpy():
   if request.method == 'POST':


         db1 = sqlite3.connect('mydatabase.db')

         def sql_insert(db1):
             cname = request.form['cname']
             email = request.form['email']
             phone = request.form['phone']
             address = request.form['address']

             sql3obj = db1.cursor()
             pointer = db1.cursor()
             sql3obj.execute("INSERT INTO student (cname,email,phone,address) VALUES('"+cname+"', '"+email+"', '"+phone+"','"+address+"')")

             db1.commit()


         sql_insert(db1)

         return render_template("home.html")
@app.route('/list')
def list():
   db1 = sqlite3.connect("mydatabase.db")
   db1.row_factory = sqlite3.Row

   pointer = db1.cursor()
   pointer.execute("select * from student")

   rows = pointer.fetchall();
   return render_template("tableedit.html",rows = rows)
   
@app.route('/delete',methods = ['POST', 'GET'])
def delete():
   if request.method == 'POST':

         db1 = sqlite3.connect('mydatabase.db')
         phone  = request.form['phone']
         sql3obj = db1.cursor()
         pointer = db1.cursor()
         sql3obj.execute("DELETE from student where phone="+phone)
         db1.commit()
   return render_template("home.html")
@app.route('/update',methods = ['POST', 'GET'])
def update():
   if request.method == 'POST':

         db1 = sqlite3.connect('mydatabase.db')
         cname = request.form['cname']
         email = request.form['email']
         phone = request.form['phone']
         address = request.form['address']
         id  = request.form['id']
         sql3obj = db1.cursor()
         pointer = db1.cursor()
         sql3obj.execute('UPDATE student SET cname = ? where id =?;',(cname,id))
         sql3obj.execute('UPDATE student SET email = ? where id =?;',(email,id))
         sql3obj.execute('UPDATE student SET phone = ? where id =?;',(phone,id))
         sql3obj.execute('UPDATE student SET address = ? where id =?;',(address,id))
         db1.commit()

   return render_template("home.html")
if __name__=='__main__':
     app.run(debug=True)
