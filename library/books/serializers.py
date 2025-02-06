from .models import Book, Loan, CustomUser

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id', 'profile_image', 'email', 'name', 'middlename', 'lastname', 'national_id', 'phone', 'date_joined', 'is_staff']

class BookSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Book
        fields = ['id', 'title', 'date', 'author', 'genre', 'description', 'orders_count','status']


class LoanSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Loan
        fields = ['id', 'owner', 'book', 'book_title', 'borrow_date', 'return_date', 'status']

