from django.db import models

class Rate(models.Model):
    metal_type = models.CharField(max_length=10)  # e.g., Gold, Silver
    rate = models.IntegerField(default=0)  # Add default value here

    def __str__(self):
        return f"{self.metal_type} : {self.rate}"
