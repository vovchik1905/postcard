import random

from django.shortcuts import render
from . import models


def index(request):
    template = 'base.html'
    return render(request, template)


def send(request):
    emails = models.EmailList.objects.all()
    email = random.choice(emails)
    template = 'pcard/chosen_email.html'
    context = {'email': email}
    return render(request, template, context)


def register(request):
    template = 'pcard/register_postcard.html'
    return render(request, template)