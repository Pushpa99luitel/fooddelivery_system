from django.db import models

class User(models.Model):
  user_id=models.AutoField(auto_created=True, primary_key=True)
  name=models.CharField(max_length=50)
  email=models.CharField(max_length=50)
  password=models.CharField(max_length=50)
  image=models.ImageField(default='img.jpg')
class Meta:
  db_table="user"

# Create your models here.
