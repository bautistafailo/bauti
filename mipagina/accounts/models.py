from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.avatar}"







