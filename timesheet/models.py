from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your models here.

class Customer(models.Model):
    """Model representing a customer (e.g. a company)."""
    name = models.CharField(max_length=200,
                            unique=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this customer."""
        return reverse('customer-detail', args=[str(self.id)])

class Project(models.Model):
    """Model representing a project (e.g. a device, a PCB)."""
    name = models.CharField(max_length=200,
                            unique=True)

    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this customer."""
        return reverse('project-detail', args=[str(self.id)])

class Entry(models.Model):
    """Model representing a timesheet entry"""

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """String for representing the Model object."""
        return str(self.date)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this entry."""
        return reverse('entry-detail', args=[str(self.id)])
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    duration = models.DecimalField(decimal_places=1, max_digits=3)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)

