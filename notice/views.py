from django.shortcuts import render
from django.http import HttpResponse

 
def list(request):
    return render(request, 'notice/list.html')

def write(request):
    return render(request, 'notice/write.html')