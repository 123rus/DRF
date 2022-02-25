from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Контент')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title