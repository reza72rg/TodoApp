from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from accounts.models import User, Profile
from todo.models import Status, Task
import random
status_list = [
    "It",
    "Design",
    "Fun",
]

class Command(BaseCommand):
    help = "Insert dump data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()
    def handle(self, *args, **options):
        user = User.objects.create_user(
        email=self.fake.email(), password="123456789ab"
        )
        profile = Profile.objects.get(user = user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.descriptions = self.fake.paragraph(nb_sentences= 5)
        profile.save()
        
        for item in status_list:
            Status.objects.get_or_create(name = item)
        
        for _ in range(10):
            Task.objects.create(
                author = profile,
                title = self.fake.paragraph(nb_sentences= 1),
                description = self.fake.paragraph(nb_sentences= 5),
                status = Status.objects.get(name=random.choice(status_list)),
            )