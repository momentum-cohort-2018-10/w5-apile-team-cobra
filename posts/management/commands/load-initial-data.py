from django.core.management.base import BaseCommand


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

    def create_posts(self):
        print("deleted posts")
        Post.objects.all().delete()

        print("created posts")
        posts = []

        for post_data in intitial_posts:
            

    def handle(self, *args, **options):
        
                
