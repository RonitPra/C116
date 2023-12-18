# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/me")
def home():

    name = "Ronit" # write your name
    age = "15" # write your age
    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Prashanth" # write your name
    age = "47" # write your age
    return render_template('father.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Amrita" # write your name
    age = "45" # write your age
    return render_template('mother.html' , name = name , age = age)

@app.route("/friend")
def friend():

    name = "Emanuel" # write your name
    age = "15" # write your age
    return render_template('friend.html' , name = name , age = age)

C:\Users\prash\Downloads\PRO-C116-Project-Boilerplate-main\PRO-C116-Project-Boilerplate-main\family tree\FamilyTree
# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
