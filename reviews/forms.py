from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('developer', 'reviewer', 'review_date', 'review_status', 'dispute_comment', 'dispute_history')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'review_header': 'Review Title',
            'review_body': 'Review',
            'review_rating': 'Developer Rating',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

