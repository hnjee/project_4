from django.shortcuts import render
from django.http import HttpResponse

 
def list(request):
    #Data 전달
    context = {'board':'notice', 'age':20}
    return render(request, 'notice/list.html', context)

def write(request):
    return render(request, 'notice/write.html')