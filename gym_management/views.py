from django.template import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template("gym_management/index.html")
    return HttpResponse(template.render())

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm

def register_member(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new member object
            return redirect('success_url')  # Redirect to success page
    else:
        form = MemberRegistrationForm()

    context = {'form': form}
    return render(request, 'member_registration.html', context)
