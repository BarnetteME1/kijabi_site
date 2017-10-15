from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class culture_info(models.Model):
    #author = models.ForeignKey(User)
    timestampe = models.DateTimeField(auto_now_add=True)
    bacteria_type = models.CharField(max_length=10)
    culture_results = models.CharField(max_length=3)
    culture_site = models.CharField(max_length=25)
    Diagnosis = models.TextField()
    ward = models.CharField(max_length=25)
    med_department = models.CharField(max_length=25)
    device = models.CharField(max_length=1)
    device_duration = models.IntegerField()
    patient_number = models.IntegerField()
    previous_admission = models.CharField(max_length=1)
    previous_discharge_date = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField(User)

    @receiver(post_save, sender=User)
    def user_post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        created = kwargs.get('created')
        if created:
            Profile.objects.create(user=instance)
