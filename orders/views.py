from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from product.models import city
from .forms import OrderForm
from product.models import Savat
from django.urls import reverse_lazy
import stripe
from django.conf import settings
from django.urls import reverse

# Create your views here.
class CreateOrderView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('payment')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateOrderView, self).form_valid(form)

def IndexView(request):
    return render(request, 'index.html')

def PaymentView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1OhqaiHVlKmVyU1G8vkfc78W',
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            payment_method_types=['card'],
            success_url = request.build_absolute_uri(reverse('success')),
            cancel_url = request.build_absolute_uri(reverse('order_create')))
    context = {
        'session_id': checkout_session.id, 
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    
    return redirect(checkout_session.url, code=303,context=context)

def SuccessView(request):
    return render(request, 'success.html')

def CancelView(request):
    return render(request, 'cancel.html')
