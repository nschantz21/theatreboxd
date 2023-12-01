from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()

    def validate_dates(self):
        return self.date_of_birth <= self.date_of_death

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    name = models.CharField(max_length=64)
    # the address will probably need to be replaced by a more formal field
    address = models.CharField(max_length=256)

class Show(models.Model):
    title = models.CharField(max_length=128)
    year = models.DateField(verbose_name="Initial Run")
    # add image
    # image = models.ImageField()

    def __str__(self):
        return f"{self.title} ({self.year})"


class Production(models.Model):
    start_date = models.DateField(verbose_name="opening date")
    end_date = models.DateField(verbose_name="closing date")  # can be null
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.show.title}, {self.start_date} to {self.end_date}"


class Performance(models.Model):
    performance_date = models.DateField(verbose_name="performance date")
    production = models.ForeignKey(Production, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.production}: {self.performance_date}"

class Stars(models.Model):
    # TODO: look at using the choice model
    star = models.IntegerField()
    # and then you need to populate with stars 1-5
    def __str__(self):
        return "*"*self.star

class Rating(models.Model):
    stars = models.ForeignKey(Stars, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024, null=True)

    # TODO: I believe there is a special syntax for a multi-column primary key
    # restrict this to one submission per user per performance

    def __str__(self):
        c = "" if not self.comment else self.comment
        return f"{self.stars}: " + c[:32]

class CastCrew(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="agent")
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show")
    production = models.ForeignKey(Production, on_delete=models.CASCADE, related_name="production")
    role = models.CharField(max_length=64, null=False)


    list_display = ('show', 'agent')

    def __str__(self):
        return f"{self.agent}-{self.show}"
