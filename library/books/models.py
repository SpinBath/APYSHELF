from django.contrib.auth.models import Group, User

from django.db import models


# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title}'