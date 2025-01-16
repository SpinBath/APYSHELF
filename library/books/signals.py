
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CustomUser, Book

@receiver(post_migrate)
def create_default_user(sender, **kwargs):

    if not CustomUser.objects.filter(email='admin@apyshelf.com').exists():

        CustomUser.objects.create_admin(
            email='admin@apyshelf.com',
            name='admin',
            password='admin'
        )
    
    if not CustomUser.objects.filter(email='johndoe@example.com').exists():

        CustomUser.objects.create_user(
            email='johndoe@example.com',
            name='John',
            middlename='M.',
            lastname='Doe',
            national_id='987987987z',  
            phone='923923923',       
            password='password123'    
        )

@receiver(post_migrate)
def create_default_book(sender, **kwargs):
    if not Book.objects.filter(title='1984').exists():

        Book.objects.create(
            title='1984',
            author='George Orwell',
            date='1949-06-08',  
            genre='Dystopian Fiction',  
            description=(
                'A dystopian social science fiction novel and cautionary tale about the future of society.'
            )
        )

    if not Book.objects.filter(title='To Kill a Mockingbird').exists():

        Book.objects.create(
            title='To Kill a Mockingbird',
            author='Harper Lee',
            date='1960-07-11',  
            genre='Southern Gothic, Drama',  
            description=(
                'A novel about the serious issues of rape and racial inequality, '
                'narrated by the young Scout Finch in the Deep South of the 1930s.'
            )
        )
    
    if not Book.objects.filter(title='Pride and Prejudice').exists():

        Book.objects.create(
            title='Pride and Prejudice',
            author='Jane Austen',
            date='1813-01-28',  
            genre='Romantic Fiction',  
            description=(
                'A classic novel of manners that explores the issues of class, marriage, and morality in early 19th-century England.'
            )
    )