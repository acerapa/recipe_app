from datetime import datetime
from msilib.schema import tables
from pydoc import classname
from unicodedata import name
from django.db import models
from account.models import Account
from file.models import File as MasterFile
from bookmarks.models import Bookmark as MasterBookmark
from procedure.models import Procedure as MasterProcedure
from comments.models import Comment as MasterComment

# Create your models here.
class Recipe(models.Model):
  class Meta:
    db_table = 'recipes'
    
  user = models.ForeignKey(name='user_id',to= Account, on_delete=models.CASCADE)
  file = models.ForeignKey('file.File', name="file_id" ,on_delete=models.CASCADE, default=None)
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
  
# inherited class
class AdminProcedures(MasterProcedure):
  class Meta:
    verbose_name_plural = 'Procedures'
    db_table = 'procedures'

class AdminBookmarks(MasterBookmark):
  class Meta:
    verbose_name_plural = 'Bookmarks'
    db_table = 'bookmarks'

class AdminComments(MasterComment):
  class Meta:
    verbose_name_plural = 'Comments'
    db_table = 'comments'
class AdminFiles(MasterFile):
  class Meta:
    verbose_name_plural = 'Files'
    db_table = 'files'
