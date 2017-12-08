from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def user_form():
	return render_template("index.html")

@app.route('/results', methods = ['POST'])
def create_user_info():
	errors = False

	email = request.form['email']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['password']
	confirm_password = request.form['confirm_password']

	if len(email) < 1 or len(first_name) < 1 or len(last_name) < 1 or len(password) < 1 or len(confirm_password) < 1:
		flash("Fields cannot be empty!")
		errors = True
	if not EMAIL_REGEX.match(email):
		flash("Invalid Email Address")
	if not first_name.isalpha() or not last_name.isalpha():
		flash("First/last name has a non-alpha character")
		errors = True
	if len(password) < 8:
		flash("Password is too short")
		errors = True
	if password != confirm_password:
		flash("Passwords don't match")
		errors = True

	if errors == False:
		flash('Success!')

	return redirect('/')

app.run(debug=True)