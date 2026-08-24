from django.test import TestCase
from .models import Member
class MemberModelTest(TestCase):
    def test_create_member(self):
        member = Member.objects.create(name="John Smith", email="john@example.com", phone="9876543210")
        self.assertEqual(Member.objects.count(), 1)