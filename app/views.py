from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    name=request.GET.get('name')
    message=request.GET.get('message')

    context={
        'name':name,
        'message': message
    }
    return render(request,'main.html',context=context)