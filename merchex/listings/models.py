from django.db import models
from django.core.validators import MinValueValidator
class ListingType(models.TextChoices):
    CONCERT = "CONCERT", "Concert"
    ALBUM = "ALBUM", "Album"
    MERCH = "MERCH", "Merchandise"
    MISC = "MISC", "Miscellaneous"

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = "HH", "Hip Hop"
        SYNTH_POP = "SP", "Synth Pop"
        ALTERNATIVE_ROCK = "AR", "Alternative Rock"

    name = models.CharField(max_length=100)
    genre = models.CharField(default="Unknown",choices=Genre.choices, max_length=100)
    biography = models.CharField(default="No Biography available", max_length=255)
    year_formed = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900)])
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)
    description = models.CharField(default="A definir ",max_length=255)
    sold = models.BooleanField(default=True)
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1900)])
    type = models.CharField(max_length=20, choices=ListingType.choices, default=ListingType.MISC)  # Type d'annonce ajouté
    def __str__(self):
        return self.name

