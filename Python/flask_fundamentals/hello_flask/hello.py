#import flask to allow us to create our app and import
#render_template allows us to render index.html
# from flask import Flask, render_template 
# #global variable __name__ tells Flask whether or not we
# # are running the file directly or importing it as a module
# app = Flask(__name__)
# #the "@" symbol designates a 'decorator' which attaches the
# #following function to the '/' route. this means that whenever
# #we send a request to localhost:5000/ we will run the
# #following 'hello_world' function.
# @app.route('/')

# def hello_world():
# 	#render the template and return it
# 	return render_template('index.html')
# #run the app in debug mode
# app.run(debug=True)


# @app.route('/success')
# def success():
# 	return render_template('success.html')

from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
	return 'Hello World!'
app.run(debug=True)