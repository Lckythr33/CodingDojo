from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL   # import the function that will return an instance of a connection
from flask_bcrypt import Bcrypt 
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
    	flash("Please enter a first name")
    if len(request.form['last_name']) < 1:
    	is_valid = False
    	flash("Please enter a last name")
    if len(request.form['email']) < 4:
    	is_valid = False
    	flash("Email should be at least 2 characters")
    if (request.form['password'] != request.form['confirm']):
    	is_valid = False
    	flash("Passwords do not match!")

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
    
        print(request.form)
        flash("User successfully added!")
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
            flash("User successfully logged in!")
        else:
            flash("Correct email, wrong password!")
    else:
        flash("Invalid Credentials!")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

