from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.

def index(request):
  return render(request, 'survey/index.html')


def process_form(request):
  try:
    request.session['counter'] = 0
  except:
    request.session['counter'] += 1

  print request.session['counter']


  content = {
    "name" : request.POST['name'],
    "location" : request.POST['location'],
    "langauge" : request.POST['language'],
    "comment" : request.POST['comment']
  }




  return render(request, 'survey/result.html', content)

