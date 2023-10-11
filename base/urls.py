from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

    path('profile/<str:username>/', views.user_profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('donate_book/', views.donate_book, name='donate_book'),
    path('donate_material/', views.donate_material, name='donate_material'),
    #path('donate_to_institution/', views.donate_to_institution, name='donate_to_institution'),
    path('free_books/', views.free_books, name='free_books'),
    path('priced_books/', views.priced_books, name='priced_books'),
    path('free_material/', views.free_material, name='free_material'),
    path('priced_material/', views.priced_material, name='priced_material'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

