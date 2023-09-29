from django.db import models

# Create your models here.
#ENUM
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class movie(models.Model):
    UID = models.UUIDField #Computer fields

    # Business fields
    movie_id = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=15)

    class Meta:
        ordering = ['movie_id']

    def __str__(self):
        return self.movie_id + '  ' + self.movie_name