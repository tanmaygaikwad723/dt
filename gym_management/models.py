from django.db import models

# Create your models here.
class Trainer(models.Model):
    choice = {
        "m": "male",
        "f": "female",
        "o": "other"
    }
    name = models.CharField(max_length=30),
    address = models.CharField(max_length=100),
    city = models.CharField(max_length=30),
    gender = models.CharField(max_length=1, choices=choice, default="m"),
    date_of_birth = models.DateField(),
    email = models.EmailField(),
    jod = models.DateField(),
    trainspec = models.CharField(max_length=30),
    experience = models.DecimalField(),
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name},\t{self.gender}\t{self.DOB}\t{self.phone}\t{self.trainspec}"
        