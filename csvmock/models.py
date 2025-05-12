from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields like address, email, etc. if needed

    def __str__(self):
        return self.name


class CompanyLocation(models.Model):
    company = models.ForeignKey(Company, related_name='locations', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.address} ({self.company.name})"


class Permission(models.Model):
    permission_name = models.CharField(max_length=100)
    permission_id = models.PositiveIntegerField(unique=True)
    users = models.ManyToManyField(User, related_name='custom_permissions')

    def __str__(self):
        return self.permission_name