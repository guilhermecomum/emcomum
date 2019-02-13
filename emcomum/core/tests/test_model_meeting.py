from datetime import datetime
from django.test import TestCase
from emcomum.core.models import Meeting


class MeetingModelTest(TestCase):
    def setUp(self):
        self.obj = Meeting(
            host_name='Tom Jobim',
            host_email='tom@mpb.br',
            guest1_name='Miles Davis',
            guest1_email='miles@jazz.com',
            guest2_name='Baden Powell',
            guest2_email='baden@mpb.br',
            message='Olá'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Meeting.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
