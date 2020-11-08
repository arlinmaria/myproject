from django.shortcuts import render
from django.http import HttpResponse
def myfun(request):
	return HttpResponse("hellow world")
def myfun1(request):
	return HttpResponse("<h1> my </h1>")
def myfunction(request):
    return render(request,'sample.html')	
