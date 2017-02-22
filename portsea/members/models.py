from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from custom_user_official.models import MyUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_of', null=True, blank=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    club = models.ForeignKey('club.Club', null=True, blank=True, default=None)


    def __str__(self):
        if self.user:
            first_name = self.user.first_name
            last_name = self.user.last_name
            name = "%s %s" % (first_name, last_name)
            return name
        else:
            return "-"