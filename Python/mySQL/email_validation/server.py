from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/results', methods=['POST'])
def check_email():
	email = request.form['email']
	errors = False
	query = "SELECT * FROM user ORDER BY created_at DESC"
	user = mysql.query_db(query)

	if len(email) < 1:
		flash("Email address cannot be empty!")
		errors = True
	if not EMAIL_REGEX.match(email):
		flash("Invalid Email Address")
		errors = True

	if errors == True:
		return redirect('/')

	if errors == False:
		query = "INSERT INTO user (email, created_at) VALUES (:email, NOW())"
	# We'll then create a dictionary of data from the POST data received.
	data = {
		'email': email,
	}
	mysql.query_db(query, data)
	return render_template('results.html', email=email, all_emails=user)


app.run(debug=True)
