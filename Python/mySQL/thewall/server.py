from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii # include this at the top of your file
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
	# session['loggedin'] = False
	return render_template("index.html")

#REGISTRATION VALIDATION
@app.route('/results', methods = ['POST'])
def create_user_info():
	errors = False
	salt = binascii.b2a_hex(os.urandom(15))
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
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
			query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
			data2 = {
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
				'password': md5.new(password + salt).hexdigest(),
				'salt': salt
			}
			user_id = "SELECT * FROM users WHERE email = :email"
			session["user_id"] = user_id

		mysql.query_db(query, data2)
		return redirect('/wall')

	return redirect('/')

#LOGIN VALIDATION
@app.route('/wall', methods = ['POST'])
def log_in():
	errors = False
	email = request.form['email']
	password = request.form['password']
	salt = binascii.b2a_hex(os.urandom(15))

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
			for user in (mysql.query_db(check, data)):
				salt = user['salt']
				hashed_password = md5.new(password + salt).hexdigest()
				if hashed_password == user['password']:
					session['user_id'] = user['id']
					session['user_name'] = user['first_name']
					return redirect("/wall")
				else:
					flash("Login failed")
	return redirect('/')



@app.route('/wall')
def wall():
	message_query = "SELECT users.first_name, users.last_name, messages.created_at, messages.message, messages.id FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.created_at DESC"
	messages = mysql.query_db(message_query)

	name_query = "SELECT users.first_name FROM users LIMIT 1"
	names = mysql.query_db(name_query)

	comment_query = "SELECT users.first_name, comments.comment, comments.created_at, comments.id, messages.id, comments.message_id FROM users LEFT JOIN comments ON users.id = comments.user_id LEFT JOIN messages ON comments.user_id = messages.user_id"
	comments = mysql.query_db(comment_query)

	# return render_template('wall.html', all_messages=messages, all_names=names)
	return render_template('wall.html', all_messages=messages, all_names=names, all_comments=comments)

#ADDS MESSAGE TO WALL
@app.route('/post_message', methods=['POST'])
def post_message():
	errors = False
	message = request.form['message_to_post']

	if len(message) < 1:
		flash("Message cannot be empty")
		errors = True
		return redirect('/wall')
	
	if errors == False:
		query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
		message_data = {'message': message, 'user_id': session['user_id']}
		mysql.query_db(query, message_data)
		return redirect('/wall')

	return redirect('/wall')

#ADDS COMMENT TO WALL
@app.route('/post_comment/<id>', methods=['POST'])
def post_comment(id):
	errors = False
	comment = request.form['comment_to_post']

	if len(comment) < 1:
		flash("Comment cannot be empty")
		errors = True
		return redirect('/wall')
	
	if errors == False:
		comment_query = "INSERT INTO COMMENTS (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"
		comment_data = {'comment': comment, 'user_id': session['user_id'], 'message_id': id}
		mysql.query_db(comment_query, comment_data)
		return redirect('/wall')

	return redirect('/wall')

#LOG OUT
@app.route('/log_out', methods=['POST'])
def log_off():
	session.pop('user_id')
	return redirect('/')


app.run(debug=True)