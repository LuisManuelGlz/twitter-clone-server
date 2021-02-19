from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, password=None):
        user = self.create_user(
            username=username,
            email=email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_admin = models.BooleanField(verbose_name='Admin status', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.URLField(
        default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y')
    location = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=160, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    following = models.ManyToManyField(
        'self', blank=True, related_name='profile_following', symmetrical=False)
    following_total = models.IntegerField(default=0)
    followers = models.ManyToManyField(
        'self', blank=True, related_name='profile_followers', symmetrical=False)
    followers_total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} profile"


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    # Create profile after user is created
    if kwargs.get('created', False):
        Profile.objects.create(user=instance, location='', bio='', website='')
