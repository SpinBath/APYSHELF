from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):

     def create_user(self, email, name, middlename, national_id, phone, password=None, **extra_fields):
       
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
            phone=phone,
            **extra_fields
        )

        user.set_password(password)  

        user.save(using=self._db)

        return user
     
     def create_admin(self, email, name, password=None, **extra_fields):
       
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            name=name, 
            **extra_fields
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

    book_choices = (("Available", "Available"),
                    ("Not Available", "Not Available"),
                    ("On hold", "On hold"))

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    orders_count = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=book_choices, default="Available")

    def save(self, *args, **kwargs):

        if self.orders_count == 0:
            self.status = "Available"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Loan(models.Model):

    loan_choices = (("Accepted", "Accepted"),
                    ("Rejected", "Rejected"),
                    ("On hold", "On hold"))

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=loan_choices, default="On Hold")

    def __str__(self):
        return f'{self.book.title}'