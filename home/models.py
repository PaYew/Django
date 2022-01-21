from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class posty(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    context_object_name = 'posty'
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    like = models.IntegerField(default=0)