from django.test import TestCase
from django.contrib.auth.models import User

class YourTest(TestCase):
    def test_add_docs(self):
        # If you already have another user, you might want to use it instead
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')

        # self.client.login sets up self.client.session to be usable
        self.client.login(username='admin', password='admin')

        session = self.client.session
        session['documents_to_share_ids'] = [1]
        session.save()

        response = self.client.get('/')  # request.session['documents_to_share_ids'] will be available