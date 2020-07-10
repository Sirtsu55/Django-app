from django.db import models
from datetime import datetime
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    display_summary = models.TextField(max_length = 500, default = 'Summary of article')
    date_added = models.DateTimeField('date published', default = datetime.now())
    def __str__(self):
        return self.title

