from django.db import models
from django.forms import ModelForm

TITLE_CHOICES=(('MR','Mr.'),('MRS','Mrs.'),('MS','Ms'),)
class Author(models.Model):
  name=models.CharField(max_length=100)
  title=models.CharField(max_length=3,choices=TITLE_CHOICES)

  def __str__(self):
    return self.name

class Book(models.Model):
  name=models.CharField(max_length=100)
  authors=models.ManyToManyField(Author)

class AuthorForm(ModelForm):
  class Meta:
    model=Author
    fields=['name','title']

class BookForm(ModelForm):
  class Meta:
    model=Book
    fields=['name','authors']

