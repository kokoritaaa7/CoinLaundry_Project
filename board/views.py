from django.shortcuts import render

def index(request):
    print("test")
    return render(request,'base.html')

def test(request):
    return render(request, 'account.html')
