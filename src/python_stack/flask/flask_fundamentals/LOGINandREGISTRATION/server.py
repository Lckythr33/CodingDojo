from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL   # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key="so secret"
@app.route("/")
def new_user():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def create_user():
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
    
    if not is_valid:
        return redirect("/")
    else:   
    	# add user to database
        mysql = connectToMySQL('loginDB')	 
        data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password']
        }
        query = "INSERT INTO `logindb`.`users` (`first_name`, `last_name`, `email`, `password`) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = mysql.query_db(query, data)
    
        print(request.form)
        flash("Friend successfully added!")
        return redirect('/') # either way the application should return to the index and display the message
   


if __name__ == "__main__":
    app.run(debug=True)