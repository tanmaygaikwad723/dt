from django import forms
from .models import Member, Trainer, WeightRecord

choice = [
        ("m", "male"),
        ("f", "female"),
        ("o", "other"),
    ]
subs = [
        ("M", "monthly"),
        ("Q", "Quarterly"),
        ("A", "Annualy"),
    ]

class MemberRegistrationForm(forms.ModelForm):
    trainer = forms.ModelChoiceField(queryset=Trainer.objects.all())
    class Meta:
        model = Member
        fields = ['name', 'trainer', 'age', 'sex', 'weight', 'height', 'address', 'subscription', 'fees']
        widgets = {
            'sex': forms.Select(choices=choice),
            'subscription': forms.Select(choices=subs),
            'fees': forms.Select(choices=[("P", "paid"), ("NP", "Not_paid")])
        }


class Weightregisterform(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=Member.objects.order_by("name"))
    class Meta:
        model = WeightRecord
        fields = ['member', 'date', 'weight']
        widgets = {
            'date': forms.SelectDateWidget(),
        }


class Member_select_form(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=Member.objects.all().order_by("name"))
    class Meta:
        model = Member
        fields = ["name"]