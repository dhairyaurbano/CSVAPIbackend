from django.db import models

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
