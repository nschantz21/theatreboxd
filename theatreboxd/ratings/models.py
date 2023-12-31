from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(default="1899-01-01")
    date_of_death = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    name = models.CharField(max_length=64)
    # the address will probably need to be replaced by a more formal field
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Show(models.Model):
    title = models.CharField(max_length=128)
    year = models.DateField(verbose_name="Year of Initial Run")
    # add image
    # image = models.ImageField()

    def __str__(self):
        return f"{self.title} ({self.year.year})"


class Production(models.Model):
    # there aren't always previews
    preview_start_date = models.DateField(verbose_name="previews date", blank=True, null=True)
    start_date = models.DateField(verbose_name="opening date")
    end_date = models.DateField(verbose_name="closing date", blank=True, null=True)  # can be null
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.show.title}, {self.start_date} to {self.end_date}"


class Performance(models.Model):
    performance_datetime = models.DateTimeField(verbose_name="performance date")
    production = models.ForeignKey(Production, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.production}: {self.performance_datetime}"

class Star(models.Model):
    star = models.IntegerField()
    # and then you need to populate with stars 1-10:
    # it's really 10 stars bc of the half stars
    def __str__(self):
        return "*"*self.star

class Rating(models.Model):
    stars = models.ForeignKey(Star, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024, null=True)

    # TODO: I believe there is a special syntax for a multi-column primary key
    # restrict this to one submission per user per performance

    def __str__(self):
        c = "" if not self.comment else self.comment
        return f"{self.stars}: " + c[:32]


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()

class Character(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name.title()


class Crew(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="agent")
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show")
    production = models.ForeignKey(Production, on_delete=models.CASCADE, related_name="production", null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, related_name="role")


    def __str__(self):
        return f"{self.agent}-{self.show}"

    def validate_dates(self):
        """
        This should check that the cast/crew association with the production contains valid performance dates

        :return:
        """
        # look up the performances
        ...

class Cast(models.Model):
    agent = models.ForeignKey(
        Crew, on_delete=models.CASCADE
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE,
        blank=True, null=True, related_name="character")
    swing = models.BooleanField(default=False)
    understudy = models.BooleanField(default=False)
