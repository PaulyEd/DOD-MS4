from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Developer, Language, Framework
from django.db.models import Q
from django.contrib import messages
from .forms import DeveloperForm

# Create your views here.


def all_developers(request):
    """ Return the all the developers available on the app """

    developers = None
    developers = Developer.objects.all()
    query = None
    queries = None
    sort = None
    direction = None
    redirect_url = request.GET.get('redirect_url')

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            developers = developers.order_by(sortkey)

        if 'framework' in request.GET:
            frameworks = request.GET['framework'].split(',')
            developers = developers.filter(framework__name__in=frameworks)
            frameworks = Framework.objects.filter(name__in=frameworks)

        if 'language' in request.GET:
            languages = request.GET['language'].split(',')
            developers = developers.filter(language__name__in=languages)
            languages = Language.objects.filter(name__in=languages)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(redirect_url)
            
            queries = Q(name__icontains=query) | Q(language__friendly_name__icontains=query) | Q(framework__friendly_name__icontains=query) | Q(spoken_language__name__icontains=query)
            developers = list(set(developers.filter(queries)))  # converting to a set then back to a list prevents object duplication for the search queries, .distict() could work similarly

    current_sorting = f'{sort}_{direction}'

    if 'framework' in request.GET:
        context = {
            'developers': developers,
            'search_term': query,
            'current_selection': frameworks,
            'current_sorting': current_sorting,
        }
    elif 'language' in request.GET:
        context = {
            'developers': developers,
            'search_term': query,
            'current_selection': languages,
            'current_sorting': current_sorting,
        }
    else:
        context = {
            'developers': developers,
            'search_term': query,
            'current_sorting': current_sorting,
        }

    return render(request, 'developers/developers.html', context)


def developer_detail(request, developer_id):
    """ Return the a requested developer to dev detail page """

    developer = get_object_or_404(Developer, pk=developer_id)

    context = {
        'developer' : developer,
    }

    return render(request, 'developers/developer_detail.html', context)

    
def add_developer(request):
    """ Add a developer to the store """
    form = DeveloperForm()
    template = 'developers/add_developer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)