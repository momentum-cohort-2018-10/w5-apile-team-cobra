from athletic_cave.settings import *
import dango_heroku

DEBUG=False


# deploy heroku settings
django_heroku.settings(locals())