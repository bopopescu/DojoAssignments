from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'Dragon'

@app.route('/')
def index():
	session['number'] = random.randrange(0, 101)
	print session['number']
	show_submit = True
	return render_template('index.html', show_submit=show_submit)

@app.route('/process', methods = ['POST'])
def submit_guess():
	user_guess = int(request.form['guess'])
	if user_guess == session['number']:
		show_all = True
		response = "YOU WIN"
		return render_template('index.html', response=response, show_all=show_all)
	elif user_guess > session['number']:
		incorrect = False
		show_submit = True
		response = "Too high"
		return render_template('index.html', response=response, incorrect=incorrect, show_submit=show_submit)
	elif user_guess < session['number']:
		incorrect = False
		show_submit = True
		response = "Too low"
		return render_template('index.html', response=response, incorrect=incorrect, show_submit=show_submit)

@app.route('/reset', methods = ['POST'])
def play_again():
	session.pop('number')
	return redirect('/')

app.run(debug=True)

