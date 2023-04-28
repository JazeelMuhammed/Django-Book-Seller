from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

RATING = (
    ('⭐', 1),
    ('⭐⭐', 2),
    ('⭐⭐⭐', 3),
    ('⭐⭐⭐⭐', 4),
    ('⭐⭐⭐⭐⭐', 5)
)

class BookReview(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book/review')
    title = models.CharField(max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    review = models.CharField(max_length=1000)
    rating = models.CharField(choices=RATING,null=True, blank=True, max_length=10)

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f'{self.title} review'

