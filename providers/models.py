"""Models for game providers"""
from django.db import models



class Provider(models.Model):
    """An entity that provides games like a Store (GOG, Humble Bundle) or a
    database (TOSEC, MobyGames).
    """
    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name

class ProviderGame(models.Model):
    """Games from providers, along with any provider specific data."""
    name = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=255)
    provider = models.ForeignKey(
        Provider,
        related_name="games",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return "[%s] %s" % (self.provider, self.name or self.slug)
