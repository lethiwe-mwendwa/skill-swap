from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

def upcoming_projects(request):
    return render(request,"upcoming_projects.html")

