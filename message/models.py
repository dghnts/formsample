from django.db import models

# Create your models here.
class Message(models.Model):
    #formのname属性に合わせる
    message = models.CharField(max_length=200)