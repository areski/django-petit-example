# from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Welcome to Django-Petit Demo</h1><br /><br />It's now %s</body></html>" % now
    return HttpResponse(html)
