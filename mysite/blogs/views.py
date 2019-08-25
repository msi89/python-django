from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    posts = ['sfk', 'rhfdss']
    return render(request, 'blogs/index.html', {'posts': posts })