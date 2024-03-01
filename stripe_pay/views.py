import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


# start page with all items shown
def index(request):
    my_list = Item.objects.all()
    return render(request, 'index.html', {'my_items_list': my_list, 'title': 'Buy me!'})


# purchase page for one item
def item(request, item_id):
    an_item = get_object_or_404(Item, id=item_id)

    if request.method == 'GET':
        context = {'item': an_item, 'title': 'Purchase', 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY}
        return render(request, 'item.html', context)


# getting stripe session_id for an item purchase
def buy(request, item_id):
    an_item = Item.objects.get(id=item_id)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': an_item.name,
                        'description': an_item.description,
                    },
                    'unit_amount': an_item.price,
                },
                'quantity': 1,
            }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({'id': checkout_session.id})


# payment was successful
class SuccessView(TemplateView):
    template_name = "success.html"


# payment failed
class CancelView(TemplateView):
    template_name = "cancel.html"
