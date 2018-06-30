from django.db import models
from django.contrib.auth.models import User

class CustomerUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    iban = models.CharField(max_length=34)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)  # admin who created this user

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
