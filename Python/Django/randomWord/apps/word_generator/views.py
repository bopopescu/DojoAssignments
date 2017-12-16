from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	try:
		request.session['counter']
	except KeyError:
		request.session['counter'] = 0
	return render(request, 'word_generator/index.html')

def word(request):
	request.session['counter'] += 1
	request.session['random_word'] = get_random_string(14)
	return redirect('/')

#to reset session
def reset(request):
	del request.session['counter']
	del request.session['random_word']
	return redirect('/')
