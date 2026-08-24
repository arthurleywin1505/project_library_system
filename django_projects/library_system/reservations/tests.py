from django.test import TestCase
from books.models import Book
from members.models import Member
from .models import Reservation
class ReservationModelTest(TestCase):
    def test_create_reservation(self):
        book = Book.objects.create(title="Clean Code", author="Robert Martin", available_copies=2)
        member = Member.objects.create(name="Asha Rao", email="asha@example.com", phone="9000000000")
        res = Reservation.objects.create(book=book, member=member, reserved_date="2026-08-23")
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(res.book.title, "Clean Code")