import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site1.settings')

import django
django.setup()

from site1_app.models import Users
from faker import Faker

faker = Faker()

def populate(N=3):
    for entry in range(N):
        fakeName = faker.name()
        fakeEmail = faker.email()

        users = Users.objects.get_or_create(name=fakeName, email=fakeEmail)[0]

if __name__ == '__main__':
    print('Populating...')
    populate(34)
    print('Populated.')