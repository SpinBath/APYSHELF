

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):

     def create_user(self, email, name, middlename, national_id, phone, password=None):
       
        if not email:
            raise ValueError("El campo 'email' es obligatorio.")
        if not name:
            raise ValueError("El campo 'name' es obligatorio.")
        if not middlename:
            raise ValueError("El campo 'middlename' es obligatorio.")
        if not national_id:
            raise ValueError("El campo 'national_id' es obligatorio.")
        if not phone:
            raise ValueError("El campo 'phone' es obligatorio.")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            name=name,
            middlename=middlename,
            national_id=national_id,
            phone=phone
        )

        user.set_password(password)  

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    national_id = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15)

    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name', 'middlename', 'national_id', 'phone']  

    def __str__(self):
        return f"{self.name} {self.middlename} ({self.lastname})"
    







class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField(max_length=300)

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Loan(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title}'