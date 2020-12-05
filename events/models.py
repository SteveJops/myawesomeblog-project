from django.db import models


# Create your models here.

class EventModel(models.Model):
    event_image = models.ImageField(upload_to='events_image/')
    event_text = models.CharField(max_length=300)
