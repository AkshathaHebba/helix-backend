from django.db import models

class Questions(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    posted_by = models.CharField(max_length=100)
    posted_date = models.DateTimeField('date published')
