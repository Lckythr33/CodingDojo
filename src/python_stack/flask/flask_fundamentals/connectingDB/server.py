from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL   # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/ninjas")
def index():
    mysql = connectToMySQL('first_flask_sql')	        # call the function, passing in the name of our db
    all_ninjas = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(all_ninjas)
    return render_template("/ninjas/index.html", all_ninjas = all_ninjas)

@app.route("/ninjas/new")
def new_ninja():
    return render_template("/ninjas/new.html")

@app.route("/ninjas", methods = ["POST"])
def create_ninja():
    mysql = connectToMySQL('first_flask_sql')	 
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name']
    }
    query = "INSERT INTO `first_flask_sql`.`friends` (`first_name`, `last_name`) VALUES (%(first_name)s, %(last_name)s);"
    mysql.query_db(query, data)
    
    print(request.form)
    return redirect("/ninjas")

@app.route('/ninjas/delete/<ninja_id>')
def delete_ninja(ninja_id):
    mysql = connectToMySQL('first_flask_sql')	        # call the function, passing in the name of our db
    data = {

        "id" : ninja_id,
    }

    query = "DELETE FROM `first_flask_sql`.`friends` WHERE `id` = %(id)s"
    mysql.query_db(query, data)
    return redirect("/ninjas")
    
if __name__ == "__main__":
    app.run(debug=True)