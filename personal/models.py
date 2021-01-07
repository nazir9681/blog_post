from django.db import models

# Create your models here.
PRIORITY = [
    ('H', 'HIGH'),
    ('M', 'MEDIUM'),
    ('L', 'LOW'),
]

STATUS_CHOICES = [
    ('0', 'Suspended'),
    ('1', 'Live'),
]

class Question(models.Model):
    title           = models.CharField(max_length=100)
    question        = models.TextField(max_length=400)
    priority        = models.CharField(max_length=1, choices=PRIORITY)

    def __str__(self):
        return self.title