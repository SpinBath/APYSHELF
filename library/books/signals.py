
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import CustomUser, CustomUserManager

@receiver(post_migrate)
def create_default_user(sender, **kwargs):

    if not CustomUser.objects.filter(email='admin@apyshelf.com').exists():

        CustomUser.objects.create_admin(
            email='admin@apyshelf.com',
            name='admin',
            password='admin'
        )
