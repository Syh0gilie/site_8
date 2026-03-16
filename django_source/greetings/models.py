from django.db import models

class Greeting(models.Model):
    surname_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} ({self.surname_id})"
