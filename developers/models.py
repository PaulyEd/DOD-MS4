from django.db import models
from django_countries.fields import CountryField


class Language(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Spoken_Language(models.Model):
    code = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)
    nativeName = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_nativeName(self):
        return self.nativeName

    class Meta:
        verbose_name = 'Spoken Language'
        verbose_name_plural = 'Spoken Languages'


class Framework(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Developer(models.Model):
    framework = models.ManyToManyField(Framework)
    language = models.ManyToManyField(Language)
    name = models.CharField(max_length=254)
    bio = models.TextField()
    tagline = models.CharField(max_length=254, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    spoken_language = models.ManyToManyField(Spoken_Language)
    website = models.CharField(max_length=254, null=True, blank=True)
    github = models.CharField(max_length=254, null=True, blank=True)
    linkedin = models.CharField(max_length=254, null=True, blank=True)
    twitter = models.CharField(max_length=254, null=True, blank=True)
    facebook = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name + str(f' - ID: {self.id}')