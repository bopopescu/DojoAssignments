from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii # include this at the top of your file
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'logreg')
app.secret_key = "ThisIsSecret"

@app.route('/')
def user_form():
	return render_template("index.html")

@app.route('/results', methods = ['POST'])
def create_user_info():
	errors = False
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	# salt = binascii.b2a_hex(os.urandom(15))
	password = request.form['password']
	confirm_password = request.form['confirm_password']

	if len(first_name) < 1:
		flash("First name cannot be empty!")
		errors = True
	elif len(first_name) < 3:
		flash("First name must be longer than 2 characters!")
		errors = True
	elif not first_name.isalpha():
		flash("First name can only contain letters!")
		errors = True

	if len(last_name) < 1:
		flash("Last name cannot be empty!")
		errors = True
	elif len(last_name) < 3:
		flash("Last name must be longer than 2 characters!")
		errors = True
	elif not last_name.isalpha():
		flash("Last name can only contain letters!")
		errors = True

	if len(email) < 1:
		flash("Email cannot be empty!")
		errors = True
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")
		errors = True

	if len(password) < 1:
		flash("Password cannot be empty!")
		errors = True
	elif len(password) < 8:
		flash("Password is too short!")
		errors = True

	if len(confirm_password) < 1:
		flash("Password cannot be empty!")
		errors = True
	elif password != confirm_password:
		flash("Passwords don't match!")
		errors = True
	
	if errors == False:
		check = "SELECT * FROM users WHERE email = :email"
		data = {"email": email}
		exists = mysql.query_db(check, data)
		if exists:
			flash("Already registered")
			return redirect('/')
		else:
			query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
			data2 = {
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
				'password': md5.new(password).hexdigest()
				#'password': md5.new(password + salt).hexdigest()
			}
			user_id = "SELECT * FROM users WHERE email = :email"
			session["user_id"] = user_id

		mysql.query_db(query, data2)
		return render_template('/success.html')

	return redirect('/')


@app.route('/login', methods = ['POST'])
def log_in():
	errors = False
	email = request.form['email']
	password = request.form['password']
	# salt = binascii.b2a_hex(os.urandom(15))

	if len(email) < 1:
		flash("Email cannot be empty!")
		errors = True
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")
		errors = True
		
	if len(password) < 1:
		flash("Password cannot be empty!")
		errors = True
	elif len(password) < 8:
		flash("Password is too short!")
		errors = True
	
	if errors == False:
		check = "SELECT * FROM users WHERE email = :email"
		data = {"email": email}
		exists = mysql.query_db(check, data)
		if not exists:
			flash("Not yet registered")
			return redirect('/')
		else:
			hashed_password = md5.new(password).hexdigest()
			for user in (mysql.query_db(check, data)):
				if hashed_password == user['password'] and user['email'] == email:
					return render_template("success.html")
				else:
					flash("Login failed")
	
	return redirect('/')


app.run(debug=True)