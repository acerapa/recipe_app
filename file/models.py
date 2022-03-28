from django.db import models
from datetime import datetime

# Create your models here.
class File(models.Model):
  # class Meta:
    # db_table = 'files'
    
  file_name = models.CharField(max_length=40)
  created_at = models.DateTimeField(default=datetime.today())
