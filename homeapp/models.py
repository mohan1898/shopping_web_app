from django.db import models
class Contactus(models.Model):
    email=models.CharField(max_length=30)
    subject=models.CharField(max_length=200)
    compliant=models.TextField(blank=True)
    def __str__(self):
        return self.email
class Home(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(upload_to='pics',blank=True,null=True)
    def __str__(self):
        return self.title
class Men(models.Model):
    category=models.CharField(max_length=200)
    def __str__(self):
        return self.category
class Menlist(models.Model):
    name=models.CharField(max_length=20)
    brand=models.CharField(max_length=30)
    price=models.IntegerField(null=True)
    men=models.ForeignKey(Men,on_delete=models.CASCADE)
    img=models.ImageField(null=True,upload_to='pics')
    def __str__(self):
        return self.name
class Women(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category
class Womenlist(models.Model):
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=80)
    price=models.IntegerField()
    women=models.ForeignKey(Women,on_delete=models.CASCADE)
    img=models.ImageField(null=True,upload_to='pics')