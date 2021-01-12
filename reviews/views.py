from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from developers.models import Developer, Language, Framework
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# Create your views here.

def add_review(request, developer_id):
    """ Add a review to a developer """
    developer = get_object_or_404(Developer, pk=developer_id)
    # if request.method == 'POST':
    #     form = DeveloperForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         developer = form.save()
    #         messages.success(request, 'Successfully added developer!')
    #         return redirect(reverse('developer_detail', args=[developer.id]))
    #     else:
    #         messages.error(request, 'Failed to add developer. Please ensure the form is valid.')
    # else:
    form = ReviewForm(instance=developer)

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'developer': developer,
    }

    return render(request, template, context)