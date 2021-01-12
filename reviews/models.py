from django.db import models
from developers.models import Developer
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Review(models.Model):
    """Model to store review related fields"""
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, blank=True)
    review_header = models.CharField(max_length=100, blank=False, default='')
    review_body = models.CharField(max_length=600, blank=False, default='')
    review_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_date = models.DateTimeField(default=timezone.now, blank=True)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)


