from django.shortcuts import render
from django.views import generic
from .models import Trainer
# Create your views here.

# def trainer_details(generic.ListView):
#     # model = Trainer
#     # context_object_name = 'Trainer_list'
#     # template_name = 'gym_management/Trainer_list.html'

def list_trainers(request):
    trainers = Trainer.objects.all()  # Get all trainer objects
    context = {'trainers': trainers}
    return render(request, 'Trainer_list.html', context)