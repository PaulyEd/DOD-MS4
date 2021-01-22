from django.db import models
from developers.models import Developer
from profiles.models import UserProfile
from django.utils import timezone

# Create your models here.

RATING_CHOICES = (
    ('1', '1 - Star'),
    ('2', '2 - Star'),
    ('3', '3 - Star'),
    ('4', '4 - Star'),
    ('5', '5 - Star'),
)

REVIEW_STATUS = (
    ('Pending', 'Pending'),
    ('Rejected', 'Rejected'),
    ('Approved', 'Approved'),
)


class Review(models.Model):
    """Model to store review related fields"""
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL,
                                  null=True, blank=True)
    review_header = models.CharField(max_length=100, blank=False, default='')
    review_body = models.TextField(max_length=600, blank=False, default='')
    review_rating = models.CharField(max_length=1,
                                     choices=RATING_CHOICES, default=0)
    review_status = models.CharField(max_length=10,
                                     choices=REVIEW_STATUS, default='Pending')
    review_date = models.DateTimeField(default=timezone.now, blank=True)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                 null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        self.review_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(f'For:{self.developer} - By:{self.reviewer}')
