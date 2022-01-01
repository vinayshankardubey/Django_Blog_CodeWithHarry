
from django.shortcuts import HttpResponse,render

# Create your views here.
def blogHome(request):
   return render(request, 'home/home.html')

def blogContact(request):
   return render(request, 'home/contact.html')

def blogAbout(request):
   return render(request, 'home/about.html')

def blogPost(request,slug):
   return HttpResponse('This is BlogPOst '+ slug)