from django.urls import path
from django.views.generic import TemplateView

from books import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('checked_out', views.checked_out, name='checked_out'),
    path('checked_in', views.checked_in, name='checked_in'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('checkin/<int:pk>', views.checkin, name='checkin'),
]