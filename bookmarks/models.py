from datetime import datetime
from django.db import models

# Create your models here.
class Bookmark(models.Model):
  # class Meta:
    # db_table = 'bookmarks'
  user_id = models.ForeignKey('account.Account', on_delete=models.CASCADE)
  recipe_id = models.OneToOneField('recipe.Recipe', on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=datetime.today())
  