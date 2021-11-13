from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.title
