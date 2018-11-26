1.)Create a repository
	-Look at getting started page
	-Use current version of Django

2.)Branch right away

3.)Model
	-Title
	-URL
	-Auto ID
	-Views.py
	-urls.py
	-templates with four loop

4.)Admin

5.)Users
	-Make, delete, edit



—Stretch Goals—

1.)Navbar
-Register
-Login
-Logout
-Title link to home

2.)Change the order of newest, least voted, highest voted, oldest

3.)CSS template

4.)Comments
Gitignore.io
From Django.contrib.auth.models import User

Class favorite(models.Model)
Post = models.ForeignKey(to=Post, on_delete = models.CASCADE)
User = (to=User, on_delete = models.CASCADE)

Class Meta:
	unique_togehter = ( ‘book’, ‘user’)