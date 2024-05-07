from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/')
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"
