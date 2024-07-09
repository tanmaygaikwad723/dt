from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.
class Trainer(models.Model):
    name = models.TextField(default="Lucifer")
    address = models.TextField(default="jane street, New York")
    city = models.TextField(default="New York")
    gender = models.TextField(default="male")
    date_of_birth = models.DateField(default=timezone.now())
    email = models.EmailField(default=None)
    jod = models.DateField(default=timezone.now())
    trainspec = models.TextField(default=None)
    experience = models.DecimalField(decimal_places=2, max_digits=2, default=0.0)
    phone = models.CharField(max_length=13, default=00000000000)

    def __str__(self):
        return f"{self.name},\t{self.gender}\t{self.date_of_birth}\t{self.phone}\t{self.trainspec}"


class Member(models.Model):
    choice = [
        ("m", "male"),
        ("f", "female"),
        ("o", "other"),
    ]
    name = models.TextField(default="anonymous")
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, default=None, null=True)
    age = models.IntegerField(default=10)
    sex = models.CharField(choices=choice, max_length=1, default="m")
    height = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=4, decimal_places=2, default=50)
    address = models.TextField(default="Jane street, New York")
    subs = [
        ("M", "monthly"),
        ("Q", "Quarterly"),
        ("A", "Annualy"),   
    ]
    subscription = models.CharField(choices=subs, max_length=10, default="M")
    fees = models.CharField(choices=[("P", "paid"),("NP", "Not_paid")], max_length=10, default="NP")