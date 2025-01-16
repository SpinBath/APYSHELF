from rest_framework import viewsets
from rest_framework import filters

from books.models import Book, Loan, CustomUser


from books.serializers import BookSerializer, LoanSerializer, UserSerializer


# View for books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'date', 'genre', 'description']
    filterset_fields = ['status']

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        if status == "Available":
            queryset = queryset.filter(status="Available")
        return queryset
    


# View for loans
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner', None)
        if owner_id is not None:
            queryset = queryset.filter(owner_id=owner_id)
        return queryset

# View for Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


  
