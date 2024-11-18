from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Member, WeightRecord
# from ludic.contrib.django import LudicResponse
# from ludic.html import html, head, body, div, h1, p, body, title, b



def home(request):
    template = loader.get_template("gym_management/index.html")
    return HttpResponse(template.render())

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm, Weightregisterform, Member_select_form

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


def dailyweightrecord(request):
    if request.method == 'POST':
        form = Weightregisterform(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            print("form is saved")
            return redirect('home')
        else:
            print("form has error")
            print(form.errors)
    else:
        form = Weightregisterform()
        
    return render(request, 'weightrecord.html', {'form': form})


def member_select_view(request):
    form = Member_select_form()
    return render(request, "show_records.html", {'form' : form})

def weight_records_view(request):
    print(request.GET.get('member'))
    member_id = request.GET.get('member_id')
    member = get_object_or_404(Member, id=member_id)
    weight_record = WeightRecord.objects.filter(member=member).order_by('date')
    return render(request, 'member_weights_list.html', {'member': member, 'weight_records': weight_record})