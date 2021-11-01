import os

os.environ.setdefault( 'DJANGO_SETTINGS_MODULE','DjangoProject.settings' )
import django

django.setup()
import random
from Blog.models import *
from faker import Faker

fakegen = Faker()
topics = ['Search','Socical','Marketplace','News','Games']


def add_topic():
    t = Topic.objects.get_or_create( top_name=random.choice( topics ) )[0]
    t.save()
    return t


def populate(N=20):
    for entry in range( N ):
        top = add_topic()
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        webpg = Webpage.objects.get_or_create( topic=top,url=fake_url,name=fake_name )[0]
        acc_rec = AccessRecord.objects.get_or_create( name=webpg,date=fake_date )[0]
if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populated')