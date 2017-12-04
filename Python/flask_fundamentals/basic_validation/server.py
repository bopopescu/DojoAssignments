from flask import Flask, render_template, redirect, request, session, flash

import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-] + \.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	#do some validations here!
	if len(request.form['email']) < 1:
		flash("Email cannot be empty!")
	elif not EMAIL_REGEZ.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("Success!")
	return redirect('/')

app.run(debug=True)