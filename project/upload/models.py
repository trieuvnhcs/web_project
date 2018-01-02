from __future__ import unicode_literals
from .validators import validate_file_extension
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=100, blank=False)
    document = models.FileField(upload_to='', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.document.name
    def delete(self , *args, **kwargs):
        self.document.delete()
        super(Document, self).delete(*args, **kwargs)

class Report(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.email
    def delete(self, *args, **kwargs):
        self.document.delete()
        super(Report, self).delete(*args, **kwargs)
