from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['gold_number'] = 0
	session['activity'] = ""
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def plus_two():
	time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
	if request.form['building'] == 'farm':
		number = random.randint(10, 20)
		session['counter'] += number
		session['activity'] += "Gained {} golds from the farm!".format(str(number)) + " " + "(" + time + ")" + '\n'
	elif request.form['building'] == 'cave':
		number = random.randint(5, 10)
		session['counter'] += number
		session['activity'] += "Gained {} golds from the cave!".format(str(number)) + " " + "(" + time + ")" + '\n'
	elif request.form['building'] == 'house':
		number = random.randint(2, 5)
		session['counter'] += number
		session['activity'] += "Gained {} golds from the house!".format(str(number)) + " " + "(" + time + ")" + '\n'
	elif request.form['building'] == 'casino':
		number = random.randint(0, 5)
		chance = random.randint(1, 2)
		if chance == 1:
			session['counter'] += number
			session['activity'] += "Gained {} golds from the casino!".format(str(number)) + " " + "(" + time + ")" + '\n'
		else:
			session['counter'] -= number
			session['activity'] += "Lost {} golds from the casino!".format(str(number)) + " " + "(" + time + ")" + '\n'

	return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] = 0
	return redirect('/')

app.run(debug=True)