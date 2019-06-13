from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL   # import the function that will return an instance of a connection
from flask_bcrypt import Bcrypt 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="so secret"
@app.route("/")
def new_user():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def create_user():
    hashed_password = bcrypt.generate_password_hash(request.form['password'])
    is_valid = True
    if len(request.form['first_name']) < 1:
    	is_valid = False
    	flash("Please enter a first name","first_name")
    if len(request.form['last_name']) < 1:
    	is_valid = False
    	flash("Please enter a last name", "last_name")
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        flash("Invalid email address!","email")
        is_valid = False
    if (request.form['password'] != request.form['confirm']):
    	is_valid = False
    	flash("Passwords do not match!","password")
    if not any(x.isupper() for x in request.form['password']):
    	is_valid = False
    	flash("Passwords needs uppercase!","upper")
    if not any(x.isdigit() for x in request.form['password']):
    	is_valid = False
    	flash("Passwords needs 1 number!","digit")

    if not is_valid:
        return redirect("/")
    else:   
    	# add user to database
        mysql = connectToMySQL('loginDB')	 
        data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_password
        }
        query = "INSERT INTO `logindb`.`users` (`first_name`, `last_name`, `email`, `password`) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = mysql.query_db(query, data)

        mysql = connectToMySQL('loginDB')	
        query = f"SELECT * FROM logindb.users WHERE id = {user_id};"
        result = mysql.query_db(query, data)
        if not "user" in session:
            session["user"] = result[0]
    
        print(request.form)
        flash("User successfully added!","registered")
        return redirect('/') # either way the application should return to the index and display the message



@app.route("/login", methods = ["POST"])
def login():
    mysql = connectToMySQL('loginDB')	 
    data = {
    'email' : request.form['email'],
    'password' : request.form['password']
    }
    query = "SELECT * FROM logindb.users WHERE email = %(email)s;"
    user = mysql.query_db(query, request.form)
   
    if user:
        user = user[0]
        if bcrypt.check_password_hash(user['password'], request.form['password']):
            flash("User successfully logged in!","loggedin")
            if not "user" in session:
                session["user"] = user
            return redirect('/')
    
        else:
            flash("Correct email, wrong password!","rightemail")
    else:
        flash("Invalid Credentials!","invalidcred")
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    flash("User successfully logout","loggedin")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

