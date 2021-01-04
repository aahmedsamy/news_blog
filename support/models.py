from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=2 ** 10)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} : {self.email}" if self.subject else self.email
