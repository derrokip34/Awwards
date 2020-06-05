from django.shortcuts import render

# Create your views here.
def home(request):

    title = 'Welcome to Awwards'
    return render(request, 'index.html',{'title':title})