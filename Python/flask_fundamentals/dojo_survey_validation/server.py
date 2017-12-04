from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def user_form():
	return render_template("index.html")

@app.route('/results', methods = ['POST'])
def create_user_info():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']

	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/')

	if len(request.form['comment']) < 1:
		flash("Comment cannot be empty!")
		return redirect('/')

	if len(request.form['comment']) > 120:
		flash("Comment cannot be longer than 120 characters")
		return redirect('/')

	return render_template('results.html', name = name, location = location, language = language, comment = comment)


app.run(debug=True)