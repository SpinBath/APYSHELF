from .models import Book, Loan, CustomUser

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id', 'email', 'name', 'middlename', 'lastname', 'national_id', 'phone', 'date_joined']

class BookSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Book
        fields = ['id', 'title', 'date', 'author', 'genre', 'available']


class LoanSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Loan
        fields = ['id', 'book', 'borrow_date', 'return_date']

