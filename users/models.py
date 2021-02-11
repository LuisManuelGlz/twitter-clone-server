from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
  name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

  REQUIRED_FIELDS = ['email']

  def save(self, *args, **kwargs):
    if not self.name:
      self.name = self.username
    self.set_password(self.password)
    super().save(*args, **kwargs)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  avatar = models.URLField(default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
  location = models.CharField(max_length=30, blank=True, null=True)
  bio = models.TextField(max_length=160, blank=True, null=True)
  website = models.URLField(max_length=100, blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
  if kwargs.get('created', False):
    Profile.objects.create(user=instance, location='', bio='', website='')
