import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        DOMAIN = "http://127.0.0.1:8000/api"
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=DOMAIN + '/success/',
            cancel_url=DOMAIN + '/cancel/',
        )

        return JsonResponse({
            'session_id': session.id
        })


class ItemDetailView(TemplateView):
    template_name = "item_detail.html"

    def get_context_data(self, **kwargs):
        item_id = self.kwargs.get('id')
        item = get_object_or_404(Item, id=item_id)
        context = super().get_context_data(**kwargs)
        context.update({
            "item": item,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
