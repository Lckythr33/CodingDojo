from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def display():
    print("in the display function") 
    return render_template("index.html")

@app.route("/play/<times>") 
def display_times(times):
    print("in the display_times function")  
    return render_template("indexMany.html",num_times=int(times))

@app.route("/play/<times>/<color>") 
def display_color(times,color):
    print("in the display_times function")  
    return render_template("indexColor.html",num_times=int(times),box_color=color)

    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.