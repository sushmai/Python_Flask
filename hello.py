# Importing Flask class 
from flask import Flask
# create app variable and set it to the instance of app class.
#__name__ == name of the module (flask knows where to look for)
app = Flask(__name__)

# route where to go on web page
# route = decorator(to add additional functionality to existing function)
# "/" = home page 
@app.route("/")
@app.route("/home")
def home():
    # what you see on page 
    return "<h1>Home Page...!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page..</h1>"

if __name__ == "__main__":
    app.run(debug = True)
