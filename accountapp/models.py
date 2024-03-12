from django.db import models

class Register(models.Model):
    email=models.EmailField(max_length=100,null=True)
    name=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
    def __str__(self):
        return self.name

