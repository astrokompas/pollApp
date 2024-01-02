from django.test import TestCase

import datetime
from django.utils import timezone
from .models import question

class questionModelTest(TestCase):
    
    def testWasPublishedRecentlyWithFutureQuestion(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days = 30)
        futureQuestion = question(pubDate = time)
        self.assertIs(futureQuestion.wasPublishedRecently(), False)
    
    def testWasPublishedRecentlyWithOldQuestion(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        oldQuestion = question(pubDate = time)
        self.assertIs(oldQuestion.wasPublishedRecently(), False)


    def testWasPublishedRecentlyWithRecentQuestion(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recentQuestion = question(pubDate = time)
        self.assertIs(recentQuestion.wasPublishedRecently(), True)

# Create your tests here.
