from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    

class Topic(models.Model):

    comment = models.CharField(verbose_name="コメント",max_length=2000)