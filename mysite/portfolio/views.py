from django.shortcuts import render

def home(request):
    return render(request,"portfolio/home.html")
def skill(request):
    return render(request,"portfolio/skill.html")
def project(request):
    return render(request,"portfolio/project.html")
def contact(request):
    return render(request,"portfolio/contact.html")
def about(request):
    return render(request,"portfolio/about.html")
