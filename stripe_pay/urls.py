from django.urls import path

from . import views
from .views import CancelView, SuccessView

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>', views.item, name='item'),
    path('buy/<int:item_id>', views.buy, name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]