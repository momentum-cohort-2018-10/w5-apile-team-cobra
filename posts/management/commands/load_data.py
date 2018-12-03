from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from posts.models import Post, Vote


intitial_posts = [
    {
        "title": "9 Fun Facts About Sporting Equipment",
        "post_link": "https://www.foodandsupplysource.com/9-fun-facts-about-sporting-equipment/",
    },
    {
        "title": "Yahoo Sports",
        "post_link": "https://sports.yahoo.com/",
    },
    {
        "title": "USA Today",
        "post_link": "https://www.usatoday.com/sports/",
    },
    {
        "title": "The New York Times, Sports",
        "post_link": "https://www.nytimes.com/section/sports",
    },
    {
        "title": "Sports Illustrated",
        "post_link": "https://www.si.com/",
    },
    {
        "title": "MSN, Sports",
        "post_link": "https://www.msn.com/en-us/sports",
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
        "title": "ESPN",
        "post_link": "http://www.espn.com/",
    },
    {
        "title": "CBS Sports",
        "post_link": "https://www.cbssports.com/",
    },
    {
        "title": "College basketball rankings",
        "post_link": "https://www.cbssports.com/college-basketball/news/college-basketball-rankings-why-texas-tech-is-13th-in-top-25-and-1-heading-into-saturdays-game-with-memphis/",
    },
    {
        "title": "NBA DFS: Joel Embiid and top picks for Dec. 2 FanDuel",
        "post_link": "https://www.cbssports.com/nba/news/nba-dfs-joel-embiid-and-top-picks-for-dec-2-fanduel-draftkings-daily-fantasy-basketball-lineups/",
    },
    {
        "title": "UFC news, rumors: Anderson Silva promised title shot",
        "post_link": "https://www.cbssports.com/mma/news/ufc-news-rumors-anderson-silva-promised-title-shot-with-win-jon-jones-not-completely-sober/",
    },
    {
        "title": "UFC Fight Night 142 predictions -- Dos Santos vs. Tuivasa",
        "post_link": "https://www.cbssports.com/mma/news/ufc-fight-night-142-predictions-dos-santos-vs-tuivasa-fight-card-odds-start-time-stream/",
    },
    {
        "title": "NBA scores, highlights",
        "post_link": "https://www.cbssports.com/nba/news/nba-scores-highlights-lebron-james-lakers-take-on-no-1-pick-deandre-ayton-suns/",
    },
    {
        "title": "College basketball recruiting",
        "post_link": "https://www.cbssports.com/college-basketball/news/college-basketball-recruiting-top-50-power-forward-akok-akok-commits-to-uconn/",
    },
    {
        "title": "Kliff Kingsbury is a godsend for USC's tantalizing offense",
        "post_link": "https://247sports.com/Article/Kliff-Kingsbury-USC-Trojans-football-JT-Daniels--125586571/",
    },
    {
        "title": "NFL odds, picks for Week 13",
        "post_link": "https://www.cbssports.com/nfl/news/nfl-odds-picks-for-week-13-advanced-computer-model-loving-chiefs-and-rams/",
    },
    {
        "title": "NFL DFS for Sunday Night Football, Week 13",
        "post_link": "https://www.cbssports.com/nfl/news/nfl-dfs-for-sunday-night-football-week-13-best-draftkings-and-fanduel-daily-fantasy-football-picks-and-lineups/",
    }, {
        "title": "Cougs get screwed by CFP committee, will not play in NY6 Bowl",
        "post_link": "https://247sports.com/college/washington-state/Article/Washington-State-football-Cougs-Cougars-NY6-New-Years-Six-College-Football-Playoff-Committee-125760066/",
    },
    {
        "title": "Steelers vs. Chargers pick, prediction, how to watch, stream",
        "post_link": "https://www.cbssports.com/nfl/news/steelers-vs-chargers-pick-prediction-how-to-watch-stram-the-james-conner-effect-melvin-gordons-absence-and-more-to-know/",
    },
    {
        "title": "MLB rumors: Mariners could move Kyle Seager using similar framework to Cano-Diaz trade",
        "post_link": "https://www.cbssports.com/mlb/news/mlb-rumors-mariners-could-move-kyle-seager-using-similar-framework-to-cano-diaz-trade/",
    },
    {
        "title": "Oregon QB Justin Herbert will play in Redbox Bowl vs. Michigan State",
        "post_link": "https://www.cbssports.com/college-football/news/oregon-qb-justin-herbert-will-play-in-redbox-bowl-vs-michigan-state-nfl-draft-intentions-unclear/",
    },
    {
        "title": "he Mets' additions of Robinson Cano and Edwin Diaz make sense as long as they commit to 2019",
        "post_link": "https://www.cbssports.com/mlb/news/the-mets-additions-of-robinson-cano-and-edwin-diaz-make-sense-as-long-as-they-commit-to-2019/",
    },
    {
        "title": "The Phillies seem interested in most of the market's top players, and here's why that's the right call",
        "post_link": "https://www.cbssports.com/mlb/news/the-phillies-seem-interested-in-most-of-the-markets-top-players-and-heres-why-thats-the-right-call/",
    },
    {
        "title": "Merciless Arsenal pounds Spurs",
        "post_link": "https://soccer.nbcsports.com/2018/12/02/merciless-arsenal-pounds-spurs-at-the-emirates/",
    },
    {
        "title": "Pickford apologizes to Everton fans for costly error vs. Liverpool",
        "post_link": "https://soccer.nbcsports.com/2018/12/02/pickford-apologizes-to-everton-fans-for-costly-error-vs-liverpool/",
    },
    {
        "title": "Insane late goal gifts Liverpool derby win",
        "post_link": "https://soccer.nbcsports.com/2018/12/02/insane-late-goal-gifts-liverpool-derby-win/",
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

        print("created posts")
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

        print('made new votes')
        for post in posts:
            # selecting a random number between 0 and 5
            num_votes = random.randint(0, 11)
            # shuffle the users
            random.shuffle(users)
            for i in range(num_votes):
                post.votes.create(user=users[i])


    def handle(self, *args, **options):
        users = self.create_users()
        posts = self.create_posts()
        votes = self.create_votes(posts, users)
