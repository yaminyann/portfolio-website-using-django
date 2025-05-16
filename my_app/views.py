from django.shortcuts import redirect,render
from django.http import request
from django.contrib import messages
from . models import *

def Home(request):
    skill_categories = Skill_Category.objects.all().prefetch_related('skills')
    project = Project.objects.all()
    experience = Experience.objects.all()

    # contact from 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        msg = Message(name=name, email=email, subject=subject, messages=message)
        msg.save()
        messages.success(request, 'Successfully send message !')
        return redirect('home')

    context = {
        'skill_categories':skill_categories,
        'project':project,
        'experience':experience,
    }
    return render(request, 'home.html', context)