from django.db import models
from django.contrib.auth.models import AbstractUser
from account.accountUserManager import AccountManager
from file.models import File

# Create your models here.
class Account(AbstractUser):
  class Meta:
    db_table = 'accounts'
    
  username = None
  email = models.EmailField('email', unique=True)
  file_id= models.ForeignKey(File, on_delete=models.CASCADE)
  
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  objects = AccountManager()
  
  def __str__(self) -> str:
      return self.email
  