from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def form():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    print("in the form function") 
    return render_template("index.html", users=users)
        
@app.route('/add_user', methods=['POST'])          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def add_user():
    print(request.form['first_name'])
    print(request.form['last_name'])
    # first_from_form = request.form['first_name']
    # last_from_form = request.form['last_name']
    # print(request.form['age'])
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.