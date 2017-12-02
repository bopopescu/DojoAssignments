from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def no_ninjas():
	return "No ninjas here"

@app.route('/ninja')
def tmnt():
	show_all = True
	return render_template('/ninja.html', show_all = show_all)

@app.route('/ninja/<ninja_color>')
def color(ninja_color):
	show_all = False
	return render_template('ninja.html', ninja_color = ninja_color, show_all = show_all)

app.run(debug=True)