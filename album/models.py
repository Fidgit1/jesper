from django.db import models

# Create your models here.


class Content(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(upload_to='Content/')
    owner = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(blank=True, null=True)
    public = models.BooleanField()

    