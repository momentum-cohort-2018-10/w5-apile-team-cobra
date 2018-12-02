from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post, Vote


intitial_posts = [
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
    {
        "title": "test",
        "post_link": "www.google.com",
    },
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

     # not working yet
    def create_posts(self):
        print("deleted posts")
        Post.objects.all().delete()

        print("creating posts")
        posts = []

        for post_data in intitial_posts:
            
            post = Post.objects.create(**post_data)
            posts.append(post)
        return posts
    # also not working
    def create_votes(self, posts, users):
        import random

        print('votes deleted')
        Vote.objects.all().delete()

        print('making new votes')
        for post in posts:
            # selecting a random number between 0 and 5
            num_votes = random.randint(0, 5)
            # shuffle the users
            random.shuffle(users)
            for i in range(num_votes):
                post.votes.create(user=users[i])


    def handle(self, *args, **options):
        users = self.create_users()
        posts = self.create_posts()
