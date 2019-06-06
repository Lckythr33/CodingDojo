from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')      # The URL FOR BROWSER AFTER LOCALHOST:5000/
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
@app.route('/repeat/<num>/<word>')
def repeatWord(num, word):
    return int(num) * word
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No Response. Try Again!."


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


    