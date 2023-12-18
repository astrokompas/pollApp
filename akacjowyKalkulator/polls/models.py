from django.db import models


class question(models.Model):
    questionText = models.CharField(max_length = 200)
    pubDate = models.DateTimeField('date published')
    

class choice(models.Model):
    question = models.ForeignKey(question, on_delete = models.CASCADE)
    choiceText = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

# Create your models here.
