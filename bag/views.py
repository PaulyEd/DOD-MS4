from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from developers.models import Developer

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified developer to the shopping bag """

    developer = get_object_or_404(Developer, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {quantity} more hours of {developer.name} to your bag. Total hours: {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {quantity} hours of {developer.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified developer to the specified amount"""

    developer = get_object_or_404(Developer, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if quantity > 0:
        bag[item_id] = quantity
        messages.info(request, f'Updated hours of {developer.name} to your bag to {quantity}')
    else:
        bag.pop(item_id)
        messages.info(request, f'Removed {developer.name} from your bag')

    request.session['bag'] = bag
    try:
        return redirect(redirect_url)
    except:
        return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    developer = get_object_or_404(Developer, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.info(request, f'Removed {developer.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)