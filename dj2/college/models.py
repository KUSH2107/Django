from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject
    

    
    