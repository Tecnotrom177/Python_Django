from django.urls import path
from recipes.views import sobre, contato, home

# HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST


urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # sobre
    path('contato/', contato),  # contato
]
