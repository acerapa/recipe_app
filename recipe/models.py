from datetime import datetime
from django.db import models
from account.models import Account
from file.models import File

# Create your models here.
class Recipe(models.Model):
  class Meta:
    db_table = 'recipes'
    
  user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
  file_id = models.ForeignKey(File, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  description = models.TextField()
  origin = models.CharField(max_length=30)
  prepared_time = models.IntegerField()
  ratings = models.DecimalField(decimal_places=2, max_digits=5)
  likes = models.IntegerField()
  dislikes = models.IntegerField()
  created_at = models.DateTimeField(default=datetime.today())
  updated_at = models.DateTimeField()
  deleted_at = models.DateTimeField()
  