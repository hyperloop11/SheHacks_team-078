from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import numpy as np
from django.urls import reverse
# Create your models here.

class College(models.Model):
    name=models.CharField(max_length=300)
    discription=models.TextField()
    rank=models.IntegerField()
    image = models.ImageField(upload_to='college_pics')
    website=models.URLField()
    address=models.CharField(max_length=400)
    is_in_wishlist=models.BooleanField(default=False)
    how_to_get_in=models.CharField(max_length=400)

    def __str__(self):
        return self.name

    def average_academics(self):
        all_academic_ratings=map(lambda x: x.academic, self.rating_set.all())
        return np.mean(list(all_academic_ratings))
    
    def average_campus(self):
        all_campus_ratings=map(lambda x: x.campus, self.rating_set.all())
        return np.mean(list(all_campus_ratings))

    def average_mess_food(self):
        all_messfood_ratings=map(lambda x: x.mess_food, self.rating_set.all())
        return np.mean(list(all_messfood_ratings))

    def average_placements(self):
        all_placement_ratings=map(lambda x: x.placements, self.rating_set.all())
        return np.mean(list(all_placement_ratings))

    def average_senior_junior_interaction(self):
        all_inter_ratings=map(lambda x: x.senior_junior_interaction, self.rating_set.all())
        return np.mean(list(all_inter_ratings))
    
    def average_coding_culture(self):
        all_coding_culture_ratings=map(lambda x: x.coding_culture, self.rating_set.all())
        return np.mean(list(all_coding_culture_ratings))

    def average_stars(self):
        all_stars=map(lambda x: x.stars, self.review_set.all())
        return np.mean(list(all_stars))

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    YEAR_CHOICES=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    author_year=models.IntegerField(choices=YEAR_CHOICES)
    academic = models.IntegerField(choices=RATING_CHOICES)
    campus = models.IntegerField(choices=RATING_CHOICES)
    mess_food = models.IntegerField(choices=RATING_CHOICES)
    placements = models.IntegerField(choices=RATING_CHOICES)
    senior_junior_interaction = models.IntegerField(choices=RATING_CHOICES)
    coding_culture = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f'{self.college} Rating'

    def get_absolute_url(self):
        return reverse('college-detail', kwargs={'pk':self.college.pk})

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    stars = models.IntegerField(choices=RATING_CHOICES)
    title=models.CharField(max_length=100)
    content = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    related_college=models.ForeignKey(College, on_delete=models.CASCADE)
    author_year=models.IntegerField()

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.ManyToManyField(College)

    def __str__(self):
        return f'{self.user.username} Wishlist'

