from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from developers.models import Developer
from profiles.models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# Create your views here.

def add_review(request, developer_id):
    """ Add a review to a developer """
    developer = get_object_or_404(Developer, pk=developer_id)
    reviewer = get_object_or_404(UserProfile, pk=request.user.id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        review = review_form.save(commit=False)
        review.developer = developer
        review.reviewer = reviewer
        try:
            review = Review.objects.get(
                    developer=developer,
                    reviewer=reviewer,
                )
            instance = get_object_or_404(Review, id=review.id)
            review_form = ReviewForm(request.POST or None, instance=instance)
            # messages.error(request, 'You have already reviewed this developer')
            if review_form.is_valid():
                review_form.save()
                messages.success(request, f'You have updated your review for {developer.name}')
                return redirect(reverse('developer_detail', args=[developer.id]))
            else:
                messages.error(request, 'Review failed, please ensure the form is valid.')
        except Review.DoesNotExist:
            if review_form.is_valid():
                review_form.save()
                messages.success(request, f'Thank you for reviewing {developer.name}')
                return redirect(reverse('developer_detail', args=[developer.id]))
            else:
                messages.error(request, 'Review failed, please ensure the form is valid.')
    else:
        review_form = ReviewForm(instance=developer)
        messages.info(request, f'You are reviewing {developer.name}')

    template = 'reviews/add_review.html'
    context = {
        'form': review_form,
        'developer': developer,
    }

    return render(request, template, context)