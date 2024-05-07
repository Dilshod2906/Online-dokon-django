from django.urls import path
from  .views import CreateOrderView,IndexView,SuccessView,CancelView,PaymentView


urlpatterns = [
    path('', CreateOrderView.as_view(), name='order_create'),
    path('orders/payment/', IndexView, name='home'),
    path('payment/',PaymentView, name='payment'),
    path('success/', SuccessView, name='success'),
    path('cancel/', CancelView, name='cancel'),
]