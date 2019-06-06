from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def hello():
    print("in the hello function")  # Return the string 'Hello World!' as a response
    return render_template("index.html")
@app.route("/<name>") 
def hello_person(name):
    print("in the hello_person function")  # Return the string 'Hello World!' as a response
    return render_template("name.html",some_name=name)
@app.route("/<name>/<times>") 
def hello_person_times(name, times):
    print("in the hello_person function")  # Return the string 'Hello World!' as a response
    return render_template("name.html",some_name=name,num_times=int(times))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.