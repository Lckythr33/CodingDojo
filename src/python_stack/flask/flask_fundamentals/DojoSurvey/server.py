from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def display():
    print("in the display function") 
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    dojo_from_form = request.form['dojo']
    lang_from_form = request.form['favorite_language']
    com_from_form = request.form['comment']
    return render_template("result.html", name_on_template=name_from_form, 
    dojo_on_template=dojo_from_form,
    lang_on_template=lang_from_form,
    com_on_template=com_from_form)


        
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.