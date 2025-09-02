from django.db import models

# Create your models here.
class Topic(models.Model):
  topic_name = models.CharField(max_length=256, unique=True)
  def __str__(self):
    return self.topic_name

class WebPage(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  name = models.CharField(max_length=256, unique=True)
  url = models.URLField(unique=True)
  def __str__(self):
    return self.name

class AccessRecord(models.Model):
  topic = models.ForeignKey(WebPage, on_delete=models.CASCADE)
  date = models.DateField()
  def __str__(self):
    return str(self.date)

class User(models.Model):
  first_Name = models.CharField(max_length=100)
  last_Name = models.CharField(max_length=100)
  email = models.EmailField()
  def __str__(self):
    return f'{self.first_Name} {self.last_Name}'
  