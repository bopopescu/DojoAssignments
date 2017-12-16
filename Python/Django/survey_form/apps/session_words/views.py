from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
	return render(request, 'session_words/index.html')

def create(request):
	# now = datetime.now().strftime('%I:%M:%S %p, %B %d, %Y')

	# request.session['word'] = request.POST['word']
	# request.session['color'] = request.POST['color']
	# request.session['big'] = request.POST.get('big', False)
	# request.session['time'] = now

	new_word = {}
	for key, value in request.POST.iteritems():
		if key != "csrfmiddlewaretoken" and key != "show-big":
			new_word[key] = value
		if key == "show-big":
			new_word['big'] = "big"
		else:
			new_word['big'] = ""
	new_word['created_at'] = datetime.now().strftime("%I:%M %S, %B %d, %Y")
	try:
		request.session['words']
	except KeyError:
		request.session['words'] = []

	temp_list = request.session['words']
	temp_list.append(new_word)
	request.session['words'] = temp_list
	
	return redirect('/session_words')

def clear(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/session_words')