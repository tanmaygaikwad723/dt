from django.shortcuts import render
from django.views import generic
from .models import Trainer
from django.template import loader

def home(request):
    template = loader.get_template("gym_management/Home.html")
    return template.render()

def list_trainers(request):
    trainers = Trainer.objects.all()  # Get all trainer objects
    context = {'trainers': trainers}
    return render(request, 'Trainer_list.html', context)