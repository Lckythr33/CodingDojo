from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL   # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('userDB')	        # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM userdb.users;')  # call the query_db function, pass in the query as a string
    print(users)
    return render_template("/users/index.html", users = users)

@app.route("/users/new")
def new_user():
    return render_template("/users/new.html")

@app.route("/users", methods = ["POST"])
def create_user():
    mysql = connectToMySQL('userDB')	 
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    query = "INSERT INTO `userdb`.`users` (`first_name`, `last_name`, `email`) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
    user_id = mysql.query_db(query, data)
    
    print(request.form)
    return redirect(f"/users/{user_id}")

@app.route('/users/delete/<user_id>')
def delete_user(user_id):
    mysql = connectToMySQL('userDB')	        # call the function, passing in the name of our db
    data = {

        "id" : user_id,
    }

    query = "DELETE FROM `userdb`.`users` WHERE `id` = %(id)s"
    mysql.query_db(query, data)
    return redirect("/users")

@app.route('/users/<user_id>')
def show_user(user_id):
    print("came in the show user func")
    mysql = connectToMySQL('userDB')
    curr_user = mysql.query_db(f"SELECT * FROM userdb.users WHERE `id` = {user_id}")
    return render_template("/users/show_user.html", curr_user = curr_user)

@app.route('/users/<user_id>/edit')
def edit_user(user_id):
    return render_template("/users/edit.html", user_id = user_id)
  
@app.route('/users/<user_id>/update', methods=["POST"])
def update_user(user_id):
    print(request.form)
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'user_id' : user_id
    }
    mysql = connectToMySQL('userDB')
    query = "UPDATE `userdb`.`users` SET `first_name` = %(first_name)s, `last_name` = %(last_name)s, `email` = %(email)s WHERE (`id` = %(user_id)s);"
    # query = "UPDATE `userdb`.`users` SET `first_name` = %(first_name)s, `last_name` = %(last_name)s, `email` = %(email)s WHERE (`id` = {user_id});"
    mysql.query_db(query,data)
    return redirect("/users")

@app.route('/users/<user_id>/destroy')
def destroy_user(user_id):
    mysql = connectToMySQL('userDB')	        # call the function, passing in the name of our db
    data = {

        "id" : user_id,
    }

    query = "DELETE FROM `userdb`.`users` WHERE `id` = %(id)s"
    mysql.query_db(query, data)
    return redirect("/users")



if __name__ == "__main__":
    app.run(debug=True)