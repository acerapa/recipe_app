from datetime import date, datetime
from django.db import models
from file.models import File
from recipe.models import Recipe

# Create your models here.
class Procedure(models.Model):
  class Meta:
    db_table = 'procedures'
    
  recipe_id = models.ForeignKey(Recipe, models.CASCADE)
  file_id = models.ForeignKey(File, models.CASCADE)
  procedure = models.TextField()
  order = models.IntegerField()
  deleted_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(default=datetime.today())
  