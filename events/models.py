from django.db import models


# Create your models here.

class EventModel(models.Model):
    event_image = models.ImageField(upload_to='events_image/')
    event_text = models.CharField(max_length=300)

    def __str__(self):
        return self.event_text[:50]
