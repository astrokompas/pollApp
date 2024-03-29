from django.db import models
from django.utils import timezone
import datetime


class question(models.Model):
    questionText = models.CharField(max_length = 200)
    pubDate = models.DateTimeField('date published')
    
    def __str__(self) -> str:
        return self.questionText
    
    def wasPublishedRecently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pubDate <= now
    

class choice(models.Model):
    question = models.ForeignKey(question, on_delete = models.CASCADE)
    choiceText = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self) -> str:
        return self.choiceText

# Create your models here.
