from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate_book/', views.donate_book, name='donate_book'),
    path('donate_to_institution/', views.donate_to_institution, name='donate_to_institution'),
    path('profile/<str:username>/', views.view_profile, name='profile'),
    path('all_books/', views.all_books, name='all_books'),
]

