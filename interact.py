from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

def get_userName():
	user_name = request.form['name']("What is your Name? ... ")
	return user_name

def greet_user(name):
    print "Welcome, " + user_name + "!"
	#print welcome <username>

def get_coffee():
    user_coffee = raw_input("What is your favourite coffee?")
    return user_coffee
    #ask user to input favourite coffee type

def get_pastry():
    user_pastry = raw_input("What is your favourite pastry?")
    return user_pastry
    #ask user to input favourite pastry

# user_name = get_userName()
# greet_user = greet_user(user_name)
# user_coffee = get_coffee()
# user_pastry = get_pastry()



# print "Great " + user_name + "! We'll get you a " + user_coffee + " and a " + user_pastry + " right away!"

app.run(debug=True)
