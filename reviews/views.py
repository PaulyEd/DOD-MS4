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



@login_required
def add_review(request, developer_id):
    """ Add a review to a developer """
    developer = get_object_or_404(Developer, pk=developer_id)
    reviewer = get_object_or_404(UserProfile, pk=request.user.id)
    users_orders = reviewer.orders.all()
    order_hist = []
    """ check if dev is in current users purchase history """
    for users_order in users_orders:
        in_history = OrderLineItem.objects.all().filter(
                     order=users_order.id, developer=developer.id)
        order_hist.append(in_history)

    if 'Dev' in str(order_hist):

        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            review = review_form.save(commit=False)
            review.developer = developer
            review.reviewer = reviewer
            review.review_status = 'Pending'
            """ If user already rated Dev, update existing review """
            try:
                review = Review.objects.get(
                        developer=developer,
                        reviewer=reviewer,
                    )
                instance = get_object_or_404(Review, id=review.id)
                review_form = ReviewForm(request.POST or None,
                                         instance=instance)
                if review_form.is_valid():
                    review_form.save()
                    review = Review.objects.get(
                        developer=developer,
                        reviewer=reviewer,
                    )
                    review.review_status = 'Pending'
                    review.save()
                    messages.success(request, f'You have updated your\
                                     review for {developer.name}')
                    return redirect(reverse('developer_detail',
                                            args=[developer.id]))
                else:
                    messages.error(request, 'Review failed, please \
                                            ensure the form is valid.')
                """ If first time reviewing dev, Add new review """
            except Review.DoesNotExist:
                if review_form.is_valid():
                    review_form.save()
                    review = Review.objects.get(
                        developer=developer,
                        reviewer=reviewer,
                    )
                    review.review_status = 'Pending'
                    review.save()
                    messages.success(request, f'Thank you for \
                                     reviewing {developer.name}')
                    return redirect(reverse('developer_detail',
                                            args=[developer.id]))
                else:
                    messages.error(request, 'Review failed, please \
                                            ensure the form is valid.')
        else:
            try:
                """ pre-populate form if updating review """
                review = Review.objects.get(
                        developer=developer,
                        reviewer=reviewer,
                    )
                instance = get_object_or_404(Review, id=review.id)
                review_form = ReviewForm(instance=instance)
                """ display blank form """
            except Review.DoesNotExist:
                review_form = ReviewForm()

            messages.info(request,
                          f'You are reviewing {developer.name}')
            template = 'reviews/add_review.html'
            context = {
                'form': review_form,
                'developer': developer,
            }
            return render(request, template, context)
    else:
        review_form = ReviewForm()
        messages.info(request, 'Sorry, only users who have purchased time \
                      with this developer can a review to their page')
        return redirect(reverse('developer_detail', args=[developer.id]))


@login_required
def delete_review(request, review_id):
    """ Delete review and update developer rating and rating count """
    review = get_object_or_404(Review, pk=review_id)
    reviewer = get_object_or_404(UserProfile, pk=request.user.id)
    developer = get_object_or_404(Developer, pk=review.developer.id)

    if not review.reviewer == reviewer:
        messages.error(request, 'Sorry, you can only delete your own reviews')
        return redirect(reverse('home'))

    if request.method == 'POST':
        review.delete()
        try:
            all_dev_reviews = Review.objects.filter(
                                   developer=developer, review_status='Approved')
            review_count = all_dev_reviews.count()
            rating_total = 0
            for all_dev_review in all_dev_reviews:
                rating_total += int(all_dev_review.review_rating)
            rating_average = float(int(rating_total)/int(
                                     review_count))
        except Exception:
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


@login_required
def review_moderation(request):
    """ show all reviews with status of pending or disputed """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    pending_reviews = Review.objects.all().filter(review_status='Pending')
    disputed_reviews = Review.objects.all().filter(review_status='Disputed')

    template = 'reviews/review_moderation.html'
    context = {
        'pending_reviews': pending_reviews,
        'disputed_reviews': disputed_reviews,
    }

    return render(request, template, context)


@login_required
def approve_review(request, review_id):
    """ approve review and flag if has been approved
    after dispute to prevent dispute spamming """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_id)
        if review.review_status == 'Disputed':
            review.dispute_history = True
        review.review_status = 'Approved'
        review.save()

        developer = get_object_or_404(Developer, pk=review.developer.id)
        all_dev_reviews = Review.objects.filter(
                          developer=developer, review_status='Approved')
        review_count = all_dev_reviews.count()
        rating_total = 0
        for all_dev_review in all_dev_reviews:
            rating_total += int(all_dev_review.review_rating)
        rating_average = float(int(rating_total)/int(
                            review_count))
        developer.rating = rating_average
        developer.save()
    return redirect(reverse('review_moderation'))


@login_required
def reject_review(request, review_id):
    """ reject a review so it will not be displayed """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_id)
        review.review_status = 'Rejected'
        review.save()
        developer = get_object_or_404(Developer, pk=review.developer.id)
        all_dev_reviews = Review.objects.filter(
                          developer=developer, review_status='Approved')
        review_count = all_dev_reviews.count()
        rating_total = 0
        for all_dev_review in all_dev_reviews:
            rating_total += int(all_dev_review.review_rating)
        rating_average = float(int(rating_total)/int(
                            review_count))
        developer.rating = rating_average
        developer.save()
    return redirect(reverse('review_moderation'))


@login_required
def dispute_review(request, review_id):
    """
    For developers to contest a review if they
    believe to be unjust or inappropriate
    """
    current_user_email = request.user.email
    review = get_object_or_404(Review, pk=review_id)
    developer = get_object_or_404(Developer, pk=review.developer.id)
    """check that current user is developer"""
    if not current_user_email == developer.email:
        messages.error(request, 'Sorry, only the developer can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        """check if review has been disputed before"""
        if review.dispute_history is True:
            messages.error(request, 'Sorry, this review has already gone \
                                    through dispute resolution process!')
            return redirect(reverse('developer_detail', args=[developer.id]))
        review.dispute_comment = request.POST.get('text')
        review.review_status = 'Disputed'
        review.save()

    messages.error(request, 'Site moderators will evaluate if \
                            this review is appropriate!')
    return redirect(reverse('developer_detail', args=[developer.id]))
