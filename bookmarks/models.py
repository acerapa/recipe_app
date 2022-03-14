from datetime import datetime
from django.db import models
from recipe.models import Recipe
from account.models import Account

# Create your models here.
class Bookmark(models.Model):
  class Meta:
    db_table = 'bookmarks'
  user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
  recipe_id = models.OneToOneField(Recipe, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=datetime.today())
  