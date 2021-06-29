from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'index1.html')

def login(request):
    return render(request,'login.html')

def pwd_reset(request):
    return render(request,'pwd_reset.html')

def account(request):
    return render(request,'account.html')

def bookmarks(request):
    return render(request, 'bookmarks.html')

def account_notifications(request):
    return render(request, 'account_notifications.html')

def account_history(request):
    return render(request, 'account_history.html')

def account_bookmarks(request):
    return render(request, 'account_bookmarks.html')


def account_cards(request):
    return render(request, 'account_cards.html')

# git test. 유재연