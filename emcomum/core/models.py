from django.db import models

class Meeting(models.Model):
    host_name = models.CharField(max_length=100)
    host_email = models.EmailField()
    guest1_name = models.CharField(max_length=100)
    guest1_email = models.EmailField()
    guest2_name = models.CharField(max_length=100)
    guest2_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
