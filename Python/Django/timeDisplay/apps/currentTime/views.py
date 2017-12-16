from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
	context = {
	"time": strftime("%b %d, %Y %-I:%M %p", gmtime())
	}
	return render(request,'currentTime/index.html', context)