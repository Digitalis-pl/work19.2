from django.urls import path
from catalog.views import contacts, main_page

urlpatterns = [
    path('', main_page),
    path('contacts/', contacts),
]
