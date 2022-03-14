from django.db import models
from recipe.models import Recipe
from account.models import Account
# Create your models here.
class Comment(models.Model):
  class Meta:
    db_table = 'comments'
  user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
  recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  comment_id = models.IntegerField()
  is_reply = models.BooleanField(default=False)
  content = models.TextField()
  likes = models.IntegerField()
  dislikes = models.IntegerField()
  