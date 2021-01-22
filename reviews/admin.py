from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_status',
        'developer',
        'review_header',
        'review_body',
        'review_rating',
        'review_date',
        'reviewer',
    )


admin.site.register(Review, ReviewAdmin)
