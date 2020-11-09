from django.shortcuts import render, get_object_or_404
from .models import Developer

# Create your views here.


def all_developers(request):
    """ Return the all the developers available on the app """

    developers = Developer.objects.all()

    context = {
        'developers' : developers,
    }

    return render(request, 'developers/developers.html', context)


def developer_detail(request, developer_id):
    """ Return the a requested developer to dev detail page """

    developer = get_object_or_404(Developer, pk=developer_id)

    context = {
        'developer' : developer,
    }

    return render(request, 'developers/developer_detail.html', context)

