from django import forms
from .models import Member, Trainer

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

