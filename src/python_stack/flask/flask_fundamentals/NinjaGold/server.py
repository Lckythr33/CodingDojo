from flask import Flask, render_template, request, redirect, session # added request
import random
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key= "mykey"
@app.route('/')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def homepage():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    print("in the homepage function") 
    return render_template("index.html")
@app.route('/process_money', methods=['POST'])
def find_gold():
    print("came in the process money method")
    if request.form['building'] == "farm":
        gold_to_add = random.randint(10,20)
        message = f"Earned {gold_to_add} from the Farm!"
    if request.form['building'] == "cave":
        gold_to_add = random.randint(5,10)
        message = f"Earned {gold_to_add} from the Cave!"
    if request.form['building'] == "house":
        gold_to_add = random.randint(2,5)
        message = f"Earned {gold_to_add} from the House!"
    if request.form['building'] == "casino":
        gold_to_add = random.randint(-50,50)
        message = f"Earned {gold_to_add} from the Casino!"

    if gold_to_add > 0:
        message = f"Earned {gold_to_add} from {request.form['building']}!"
    else:
        message = f"Lost {-gold_to_add} from the Casino!"

    session['activities'].append(message)

    session['gold'] = session['gold'] + gold_to_add
    return redirect("/")

        
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.