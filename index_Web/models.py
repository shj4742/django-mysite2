from django.db import models

# Create your models here.

class UserInfo(models.Model):

    username = models.CharField('用户名:', max_length=20, db_column='username')
    userpwd = models.CharField('密码:', max_length=64, db_column='userpwd')
