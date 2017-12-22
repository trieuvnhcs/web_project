from __future__ import unicode_literals
from .validators import validate_file_extension

from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    document = models.FileField(upload_to='', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
