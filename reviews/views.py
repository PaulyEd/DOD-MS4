from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Review
from developers.models import Developer
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from .forms import ReviewForm

# Create your views here.

@login_required
def add_review(request, developer_id):
    """ Add a review to a developer """
    developer = get_object_or_404(Developer, pk=developer_id)
    reviewer = get_object_or_404(UserProfile, pk=request.user.id)
    users_orders = reviewer.orders.all()
    order_hist = []

    for users_order in users_orders:
        in_history = OrderLineItem.objects.all().filter(order=users_order.id,
            developer=developer.id)
        order_hist.append(in_history)

    if 'Dev' in str(order_hist):

        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            review = review_form.save(commit=False)
            review.developer = developer
            review.reviewer = reviewer
            """ If user already rated Dev, update existing review """
            try:
                review = Review.objects.get(
                        developer=developer,
                        reviewer=reviewer,
                    )
                instance = get_object_or_404(Review, id=review.id)
                review_form = ReviewForm(request.POST or None, instance=instance)
                if review_form.is_valid():
                    review_form.save()

                    review_count = Review.objects.filter(developer=developer).count()
                    rating_total = Review.objects.filter(developer=developer).aggregate(Sum('review_rating'))
                    rating_average = float(int(rating_total['review_rating__sum'])/int(review_count))
                    developer.rating = rating_average
                    developer.save()

                    messages.success(request, f'You have updated your review for {developer.name}')
                    return redirect(reverse('developer_detail', args=[developer.id]))
                else:
                    messages.error(request, 'Review failed, please ensure the form is valid.')
                """ Add new review """
            except Review.DoesNotExist:
                if review_form.is_valid():
                    review_form.save()

                    review_count = Review.objects.filter(developer=developer).count()
                    rating_total = Review.objects.filter(developer=developer).aggregate(Sum('review_rating'))
                    rating_average = float(int(rating_total['review_rating__sum'])/int(review_count))
                    developer.rating = rating_average
                    developer.save()

                    messages.success(request, f'Thank you for reviewing {developer.name}')
                    return redirect(reverse('developer_detail', args=[developer.id]))
                else:
                    messages.error(request, 'Review failed, please ensure the form is valid.')
        else:
            try:
                review = Review.objects.get(
                        developer=developer,
                        reviewer=reviewer,
                    )
                instance = get_object_or_404(Review, id=review.id)
                review_form = ReviewForm(instance=instance)
                """ Add new review """
            except Review.DoesNotExist:
                review_form = ReviewForm()

            messages.info(request, f'You are reviewing {developer.name}')  
            template = 'reviews/add_review.html'
            context = {
                'form': review_form,
                'developer': developer,
            }
            return render(request, template, context)     
    else:
        review_form = ReviewForm()
        messages.info(request, 'Sorry, only users who have purchased time with this developer can a review to their page')
        return redirect(reverse('developer_detail', args=[developer.id]))


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    reviewer = get_object_or_404(UserProfile, pk=request.user.id)
    developer = get_object_or_404(Developer, pk=review.developer.id)

    if not review.reviewer == reviewer:
        messages.error(request, 'Sorry, you can only delete your own reviews')
        return redirect(reverse('home'))

    if request.method == 'POST':
        review.delete()
        try:
            review_count = Review.objects.filter(developer=developer).count()
            rating_total = Review.objects.filter(developer=developer).aggregate(Sum('review_rating'))
            rating_average = float(int(rating_total['review_rating__sum'])/int(review_count))
        except:
            rating_average = 0
        developer.rating = rating_average
        developer.save()
        messages.success(request, 'Review deleted!')
        return redirect(reverse('profile'))
    else:
        context = {
            'developer': developer,
            'confirm_delete': True,
        }
        return render(request, 'developers/developer_detail.html', context)
