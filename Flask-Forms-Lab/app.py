from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "segev(taylor's verion)"
password = "1q2w3e4r"
facebook_friends=["Elena","Yael","Avigail", "Nieky", "Romie", "Gi", "Rut"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		if username == name and password == passw:
			return redirect(url_for('home'))	
	return render_template('login.html')


@app.route('/home')  # '/' for the default page
def home():
    return render_template("home.html", lst = facebook_friends)

@app.route('/friend_exists/<string:name>', methods = ['GET', 'POST'])  # '/' for the default page
def friend_exists(name):
	check = False
	if name in facebook_friends:
		check = True
	return render_template('friend_exists.html', name_check = check, n = name)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
