from django.contrib import admin
from django.urls import path
from .views import index_view, about_view, skills_view, education_view, projects_view, contact_view
app_name='app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('skills', skills_view, name='skills'),
    path('education', education_view, name='education'),
    path('projects', projects_view, name='projects'),
    path('contact', contact_view, name='contact')
]