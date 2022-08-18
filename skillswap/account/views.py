from django.shortcuts import render

# Create your views here.


def mobile_login(request):
    return render(request,"account/mobile_login.html")
def signup(request):
    return render(request,"account/signup.html")
def manage(request):
    return render(request,"account/account_editor.html")
def account(request):
    return render(request,"account/account.html")