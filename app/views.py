from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def skills_view(request):
    return render(request, 'skills.html')

def education_view(request):
    return render(request, 'education.html')

def projects_view(request):
    return render(request, 'projects.html')

def contact_view(request):
    return render(request, 'contact.html')