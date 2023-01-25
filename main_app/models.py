from django.db import models
from datetime import date
from us import states
from django.contrib.auth.models import User
from django.urls import reverse_lazy

CATEGORIES = (
    ('CONCERTS', 'Concerts'),
    ('SPORTS', 'Sports'),
    ('ARTS_THEATER', 'Arts & Theater')
)

STATES = [(state.abbr, state.name) for state in states.STATES]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=2,
        choices=STATES,
    )
    
    def __str__(self):
        return f"{self.city}, {self.state}"

class Events(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    date = models.DateField(default=date.today)
    time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, default='', blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.location}"

class Review(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000, default='', blank=True)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.user} - {self.event}"

    def get_absolute_url(self):
        return reverse_lazy('review_list', args=[self.event.pk])







# Goes in main model to link to user
# user = models.ForeignKey(User, on_delete=models.CASCADE)