from django.test import TestCase
from .models import Book
class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(title="Django Basics", author="Jane Doe", available_copies=5)
        self.assertEqual(str(book), "Django Basics")
        self.assertEqual(Book.objects.count(), 1)