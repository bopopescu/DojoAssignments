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
	email = request.form['email']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['password']
	confirm_password = request.form['confirm_password']

	if len(email) < 1:
		flash("Email cannot be empty!")
		return redirect('/')
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")
		return redirect('/')
	if len(first_name) < 1:
		flash("First name cannot be empty!")
		return redirect('/')
	if len(last_name) < 1:
		flash("Last name cannot be empty!")
		return redirect('/')
	if len(password) < 8:
		flash("Your password is too short")
		return redirect('/')
	if len(confirm_password) < 8:
		flash("Your password is too short")
		return redirect('/')
	if password != confirm_password:
		flash("Your passwords don't match")
		return redirect('/')

	return redirect('/results')


app.run(debug=True)