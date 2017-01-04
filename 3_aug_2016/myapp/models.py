from django.db import models


class Something(models.Model):
    some_key= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    some = models.ForeignKey(Something, related_name='choice_set')
    choice_text = models.CharField(max_length=200)
