from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from todo.models import Status, Task

# import random

"""
status_list = [
    "It",
    "Design",
    "Fun",
]
"""


class Command(BaseCommand):
    help = "Insert dump data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        # Create a new user with a random email and password
        user = User.objects.create_user(
            email=self.fake.email(), password="123456789ab"
        )

        # Get the profile associated with the user
        profile = Profile.objects.get(user=user)

        # Update the profile with random first name, last name, and description
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.descriptions = self.fake.paragraph(nb_sentences=5)
        profile.save()

        """
        # Uncomment this block if you want to create status objects
        # Iterate over the status_list and create Status objects if they don't exist
        for item in status_list:
            Status.objects.get_or_create(name=item)
        """

        # Create 10 tasks with random titles, descriptions, and a status of "Completed"
        for _ in range(5):
            Task.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                description=self.fake.paragraph(nb_sentences=5),
                status=Status.objects.get(name="Completed"),
            )
