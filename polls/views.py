from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello man, I am ready to display the app</h1>")

def detail(request,question_id):
    return HttpResponse("<h1>You're looking at question %s.</h1>" % question_id)

def results(request,question_id):
    response = "<h1>You're looking at results of question %s.</h1>"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("<h1>You're looking at votes on question %s.</h1>" % question_id)