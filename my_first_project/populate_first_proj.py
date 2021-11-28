import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_first_project.settings')

import django
django.setup()

import random
from my_first_app.models import Topic,WebPage,AccessRecord

from faker import Faker
fakegen = Faker()

topics_list = ['History','Biology','Maths','Physics','Chemistry']

def add_topic() :
    t = Topic.objects.get_or_create(top_name=random.choice(topics_list))[0]
    t.save()
    return t

def populate(N=5) :

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(my_topic=top,name=fake_name,url=fake_url)[0]

        access_rec = AccessRecord.objects.get_or_create(name_in_webpage=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('Populating Script!')
    populate(15)
    print('Populating completed!')
