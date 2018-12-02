from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post, Vote


intitial_posts = [
    {
        "title": "test",
        "post_link": "www.google.com",
        "user": "test",
    }
]


class Command(BaseCommand):
    help = "Imports the initial data and creates test users"

    def add_arguments(self, parser):
        pass

    def create_users(self):
        from mimesis import Person
        print("deleted users")
        # delete all the users except the admin
        User.objects.filter(is_superuser=False).delete()

        # create new users
        print("created users")
        users = []
        person = Person()
        
        for _ in range(10):
            # for instance of User model, create a person with...
            user = User.objects.create_user(
                person.username(), 
                person.email(), 
                "password"
            )
            # add user to users list    
            users.append(user)
        return users

    # def create_posts(self):
    #     print("deleted posts")
    #     Post.objects.all().delete()

    #     print("created posts")
    #     posts = []

    #     for post_data in intitial_posts:


    def handle(self, *args, **options):
        users = self.create_users()
        
                
