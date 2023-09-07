from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

    path('profile/<str:username>/', views.user_profile, name='profile'),

    path('donate_book/', views.donate_book, name='donate_book'),
    path('donate_to_institution/', views.donate_to_institution, name='donate_to_institution'),
    path('all_books/', views.all_books, name='all_books'),
]

