from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return (f"{self.title} | {self.company} | {self.location} | {self.salary} | {self.is_active}")