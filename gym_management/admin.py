from django.contrib import admin
from .models import Trainer, Member, WeightRecord
# Register your models here.


class TrainerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "city",
        "address",
        "gender",
        "date_of_birth",
        "phone",
    ]
    

admin.site.register(Trainer, TrainerAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "trainer",
        "age",
        "weight",
        "height",
        "sex",
        "address",
        "subs",
        "subscription",
        "fees",
    ]


admin.site.register(Member, MemberAdmin)

class WeightRecordAdmin(admin.ModelAdmin):
    list_display = [ 'member', 'date', 'weight']


admin.site.register(WeightRecord, WeightRecordAdmin)