from django.db import models


#Define model for Intern
class Intern(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30, null=True)
    age = models.CharField(max_length=60, null=True)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name
