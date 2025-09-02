import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE SCRIPT
import random
from appTwo.models import AccessRecord, Topic, WebPage
from faker import Faker

fakegen = Faker()
topic_names = ['Search','Social','Marketplace','News','Games']

def add_topic():
  # t = Topic(topic_name=random.choice(topic_names))
  t = Topic.objects.get_or_create(topic_name = random.choice(topic_names))[0]
  # print(t)
  # print(type(t))
  # print(Topic.objects.all())
  t.save()
  return t

def populate(N=5):
  while N > 0:
    top = add_topic()
    # Create fake web Page and Access Record
    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()
    webpg = WebPage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]
    acc_rec = AccessRecord.objects.get_or_create(topic = webpg, date=fake_date)[0]
    N -= 1
    
if __name__ == '__main__':
  print('Populating...')
  populate(20)
  print('Populating complete!')
