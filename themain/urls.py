from django.urls import path
from . import views

urlpatterns = [
    path('', views.maqola, name='maqolalar'),
    path('create', views.create, name='create')
]