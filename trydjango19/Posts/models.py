from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)
	updated=models.DateTimeField(auto_now=False,auto_now_add=True)


	def __unicode__(self):

		return self.title

	def get_absolute_url(self):
		# return "/posts/%s"%(self.id)
		return reverse("posts:detail",kwargs={"id":self.id})