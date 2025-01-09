# Line imports flas and render_template function from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class and assign it to the variable app
app = Flask(__name__)

# Define a route for the root URL of the website
@app.route('/')
def index():
    return render_template('index.html') # Return the rendered template

# Define a route for the about page
if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode