from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello_world','number':100}
    return render(request,'webapp/index.html',context_dict)

def other(request):
    return render(request,'webapp/other.html')

def relative(request):
    return render(request,'webapp/relative.html')
