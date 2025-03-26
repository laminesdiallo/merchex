from django.db import models
from django.core.validators import MinValueValidator
class ListingType(models.TextChoices):
    CONCERT = "CONCERT", "Concert"
    ALBUM = "ALBUM", "Album"
    MERCH = "MERCH", "Merchandise"
    MISC = "MISC", "Miscellaneous"
from django.db import models
from django.core.validators import MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = "HH", "Hip Hop"
        SYNTH_POP = "SP", "Synth Pop"
        ALTERNATIVE_ROCK = "AR", "Alternative Rock"

    name = models.CharField(max_length=100)
    genre = models.CharField(choices=Genre.choices, max_length=20, default=Genre.HIP_HOP)
    biography = models.TextField(default="No Biography available")
    year_formed = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900)])
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(blank=True, default="")

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True, blank=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
