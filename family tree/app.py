# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Hailey" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name= "Lionel"
    age="39"

    return render_template("father.html", name=name, age=age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name= "Charlene"
    age="42"

    return render_template("mother.html", name=name, age=age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name= "Cassidy"
    age="16"

    return render_template("friend.html", name=name, age=age)

# add other routes, if you want

@app.route("/sister")
def sister():
    name = "Hillary"
    age = "18"

    return render_template("sister.html", name=name, age=age)

@app.route("/brother")
def brother():
    name = "Leo"
    age = "15"

    return render_template("brother.html", name=name, age=age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
