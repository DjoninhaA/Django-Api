from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField(default=0)
    user_email = models.EmailField(unique=True)

    def __str__(self):
        return f'Name: {self.user_name} | Email: {self.user_email}'
