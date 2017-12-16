from django.shortcuts import render, HttpResponse, redirect

#show form
def index(request):
	try:
		request.session['counter']
	except:
		request.session['counter'] = 0
	return render(request, 'surveys/index.html')

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	request.session['counter'] += 1

	return redirect('/result')

def result(request):
	return render(request, 'surveys/result.html')

def goBack(request):
	return redirect('/')
