from django.urls import path

from .views import (
    BuyItemView,
    ItemDetailView,
    CancelView,
    SuccessView
)

urlpatterns = [
    path('buy/<int:id>/', BuyItemView.as_view(), name='buy-item'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item-detail'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
