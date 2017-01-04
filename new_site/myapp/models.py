from django.db import models
from django.core.urlresolvers import reverse


class Something(models.Model):
    some_key= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def get_absolute_url(self):
      return reverse('myapp:detail',kwargs={'pk':self.pk})

class Choice(models.Model):
    some = models.ForeignKey(Something, related_name='choice_set')
    choice_text = models.CharField(max_length=200)
