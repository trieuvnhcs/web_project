from __future__ import unicode_literals
from .validators import validate_file_extension

from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
