from django.db import models
# Create your models here.
class Comment(models.Model):
  # class Meta:
    # db_table = 'comments'
  user_id = models.ForeignKey('account.Account', on_delete=models.CASCADE)
  recipe_id = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE)
  comment_id = models.IntegerField()
  is_reply = models.BooleanField(default=False)
  content = models.TextField()
  likes = models.IntegerField()
  dislikes = models.IntegerField()
  