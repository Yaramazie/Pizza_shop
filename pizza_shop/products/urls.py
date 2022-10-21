from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('menu/', menu, name='menu'),
    path('pizzas/', pizzas, name='pizzas'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

]
