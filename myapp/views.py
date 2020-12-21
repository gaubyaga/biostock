from django.shortcuts import render
from django.template import RequestContext


def index(request):
    return render(request, 'index.html')

def index2(request):
	return render(request, 'editas.html')
