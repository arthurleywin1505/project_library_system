from django.db import models
from books.models import Book
from members.models import Member
class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reserved_date = models.DateField()
    def __str__(self):
        return f"{self.member.name} -> {self.book.title}"