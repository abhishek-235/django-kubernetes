from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
#from django.utils.crypto import get_random_string

# $ python manage.py createadminuser --username=abhishek --email=admin@test.com --password=admin --is_superuser=1 --is_staff=1
# all arguments are optional so default values are set in the code itself.
class Command(BaseCommand):
    help = 'Create admin user'

    def add_arguments(self, parser):

        # optional arguments
        parser.add_argument('--username', type=str, help='Username to be created')
        parser.add_argument('--email', type=str, help='Email to be created')
        parser.add_argument('--password', type=str, help='Password to be created')
        parser.add_argument('--is_superuser', type=int, help='Is superuser to be created')
        parser.add_argument('--is_staff', type=int, help='Is staff user')
        

    def handle(self, *args, **kwargs):
        username = 'admin' if kwargs.get('username') is None else kwargs.get('username')
        email = 'admin@xyz.com' if kwargs.get('email') is None else kwargs.get('email')
        password = 'Admin@#@!' if kwargs.get('password') is None else kwargs.get('password')
        is_superuser = 1 if kwargs.get('is_superuser') is None else kwargs.get('is_superuser')
        is_staff = 1 if kwargs.get('is_staff') is None else kwargs.get('is_staff')

        if User.objects.count() == 0:
            User.objects.create_user(username=username, email=email, password=password, is_superuser=is_superuser, is_staff=is_staff)
        
