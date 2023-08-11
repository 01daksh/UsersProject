import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

import django
django.setup()

from appTwo.models import Users
from faker import Faker
fakegen = Faker()

def populate(n=5):


    for entry in range(n):
        fake_name = fakegen.name().split()
        fake_first_name = fakegen().name()[0]
        fake_last_name = fakegen().name()[1]
        fake_email = fakegen().email()
        user = Users.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]

if __name__ == '__main__':
    print("Populate")
    populate(20)
    print("Complete")

