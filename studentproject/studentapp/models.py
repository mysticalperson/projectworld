from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()
class member(models.Model):
    names=models.CharField(max_length=240)
    img=models.ImageField(upload_to='pic')
    desc=models.TextField()


    def __str__(self):
        return self.names