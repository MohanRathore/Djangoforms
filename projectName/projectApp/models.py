from django.db import models

# Create your models here.
class GeekModel(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.BooleanField()

    def __str__(self):
        return self.tittle
    