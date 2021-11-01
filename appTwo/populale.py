import os
import os

os.environ.setdefault( 'DJANGO_SETTINGS_MODULE','DjangoProject.settings' )
import django

django.setup()
import random
from appTwo.models import *
from faker import Faker

fake_gen = Faker()

def add_user(N=5):
    for i in range(N):
        fake_name = fake_gen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake_gen.email()

        user = User.objects.get_or_create( first_name=fake_first_name,last_name=fake_last_name,email=fake_email )[0]

if __name__== "__main__":
    print("populate data!")
    add_user(2)
