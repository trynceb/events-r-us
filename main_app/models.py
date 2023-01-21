from django.db import models
from datetime import date
from django.contrib.auth.models import User

CATEGORIES = (
    ('CONCERTS', 'Concerts'),
    ('SPORTS', 'Sports'),
    ('ARTS_THEATER', 'Arts & Theater')
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Events(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    date = models.DateField(default=date.today)
    time = models.TimeField()







# Goes in main model to link to user
# user = models.ForeignKey(User, on_delete=models.CASCADE)