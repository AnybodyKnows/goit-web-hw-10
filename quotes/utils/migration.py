import os
import django

from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "quotes.settings")
django.setup()

from quot.models import Quotes, Tag, Author # noqa

client = MongoClient(
        host="mongodb+srv://goittestdb:1234@cluster0.goh2ue4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.HW08

authors = db.author.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

