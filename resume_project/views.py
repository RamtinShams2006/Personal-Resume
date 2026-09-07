from django.shortcuts import render
from about_app.models import About
from exp_app.models import Experience
from education_app.models import Education
from certificate_app.models import Certificate

def home(request):
    about = About.objects.get(name='ramtin')
    exps = Experience.objects.all()
    educations = Education.objects.all()
    certificates = Certificate.objects.all()

    return render(request, 'index.html', context={'about':about , 'exps':exps, 'educations':educations, 'certificates':certificates})