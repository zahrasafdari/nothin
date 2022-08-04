from email.policy import default
import os
from statistics import mode
import django
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.name}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"

User=get_user_model()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to=upload_image_path, default='blank-picture.png')
    
    location=models.CharField(max_length=100 , blank=True)
    
    def __str__(self):
        return self.user.username
    