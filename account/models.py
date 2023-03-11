from django.db import models

class Users(models.Model):
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    date = models.DateField()
    fav_artist = models.CharField(max_length = 50)
    fav_genre = models.CharField(max_length = 50)

#post_1 = Users(email="Blog_1", password = "Firt Post", date = "Firt Post", fav_artist = "Firt Post", fav_genre = "Firt Post")
#post_1.save()