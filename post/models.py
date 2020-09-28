from django.db import models

# Create your models here.


class Post(models.Model):
    BOAST = 'B'
    ROAST = 'R'
    choices = [(BOAST, 'Boast'), (ROAST, 'Roast')]
    date_created = models.DateTimeField(
        auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    message = models.CharField(max_length=280)
    message_type = models.CharField(choices=choices, max_length=1)
    def __str__(self): return self.message

    def vote_total(self): return self.up_votes + self.down_votes
