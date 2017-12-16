from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'first_app/index.html')
