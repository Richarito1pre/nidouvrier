from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import uuid
from datetime import timedelta
from django.utils import timezone, timesince
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.humanize.templatetags import humanize

from datetime import datetime
from django.conf import settings
import os
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='blank-profile-picture.png')
    address = models.CharField(max_length=255, blank=True)
    group = models.CharField(max_length=255, blank=True)
    specialty = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    nature_travail = models.CharField(max_length=100, default='travail')
    lieu = models.CharField(max_length=100)
    date_travo = models.DateField()
    image = models.ImageField(upload_to='post_images', default='blank-profile-picture.png')
    type_ouvrier = models.CharField(max_length=100)
    nombre_ouvrier = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.user
    def formatted_date(self):
        return self.date_travo.strftime('%d/%m/%Y')
    def time_since_creation(self):
        now = timezone.now()
        time_difference = now - self.created_at

        if time_difference.total_seconds() < 60:
            return "Publié récemment"
        elif time_difference.total_seconds() < 3600:
            minutes = int(time_difference.total_seconds() // 60)
            return f"Publié il y a {humanize.naturaltime(self.created_at).split(',')[0]}"
        elif time_difference.total_seconds() < 86400:
            hours = int(time_difference.total_seconds() // 3600)
            return f"Publié il y a {hours} heure{'s' if hours > 1 else ''}"
        elif time_difference.total_seconds() < 2592000:
            days = int(time_difference.total_seconds() // 86400)
            return f"Publié il y a {days} jour{'s' if days > 1 else ''}"
        elif time_difference.total_seconds() < 31536000:
            months = int(time_difference.total_seconds() // 2592000)
            return f"Publié il y a {months} mois"
        else:
            years = int(time_difference.total_seconds() // 31536000)
            return f"Publié il y a {years} an{'s' if years > 1 else ''}"
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    




def get_upload_path(instance, filename):
    return os.path.join('post_images', filename)




from django.db import models

class Metier(models.Model):
    nom = models.CharField(max_length=100)
    valeur_assignee = models.IntegerField(blank=True, null=True)

