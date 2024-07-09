from django.template import loader
from django.http import HttpResponse
from .models import Member

def home(request):
    template = loader.get_template("gym_management/index.html")
    return HttpResponse(template.render())

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm

def register_member(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save() # Save the new member object
            print("form is saved")
            return redirect('home')  # Redirect to success page
        else:
            print("form has errors")
            print(form.errors)
    else:
        form = MemberRegistrationForm()

    context = {'form': form}
    return render(request, 'member_registration.html', context)
