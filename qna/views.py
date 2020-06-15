from django.shortcuts import render
 
def list(request):
    return render(request, 'qna/list.html')
def write(request):
    return render(request, 'qna/write.html')