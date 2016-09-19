from django.test import TestCase
from .models import Something
from django.test import Client
import datetime
# Create your tests here.
class MyTestCase(TestCase):

    def checking_model(self,some_key="something",pub_date='2016-12-13'):
      return Something.objects.create(some_key=some_key,pub_date=pub_date)


    def test_checking_model(self):
      s=self.checking_model()
      self.assertTrue(isinstance(s,Something))
      # self.assertEqual(s.__unicode__(),s.some_key)

    def test_list_view(self):
      # s=self.checking_model()
      # url=reverse("myapp.views.Details")
      # resp=self.client.get(url)
      # print resp

      c=Client()
      response=c.get('/')
      print response.content
      self.assertEqual(response.status_code,200)


