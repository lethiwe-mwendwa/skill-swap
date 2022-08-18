from django.shortcuts import render

# Create your views here.

def One_on_One(request):
    return render(request,"learningSpace/One_on_One.html")

def Pomodoro(request):
    return render(request,"learningSpace/pomodoro.html")
