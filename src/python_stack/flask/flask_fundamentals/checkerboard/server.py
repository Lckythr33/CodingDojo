from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/grid/<x>/<y>')          # The URL FOR BROWSER AFTER LOCALHOST:5000/
def display_grid(x,y):
    print("in the display function") 
    return render_template("index.html",grid_x=int(x), grid_y=int(y))
# @app.route('/grid/<x>/<y>/color1/color2') 
# def display_grid(x,y,color1,color2):
#     print("in the display function") 
#     return render_template("index.html",grid_x=int(x), grid_y=int(y),color_1=color1,color_2=color2)

        
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.