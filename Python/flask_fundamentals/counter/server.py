from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['count'] = 0
	try:
		session['counter'] += 1
	except: 
		session['counter'] = 0
	return render_template('index.html')

@app.route('/plus_two', methods=['POST'])
def plus_two():
	session['counter'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] = 0
	return redirect('/')


app.run(debug=True)