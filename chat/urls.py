from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern, path
from chat import views

urlpatterns = [  
    path('chat/<str:owner_name>/', views.chat, name='chat'),
    path('all_chats/', views.all_chats, name='all_chats'),
    path('receiver_chat/<str:receiver>/', views.receiver_chat, name='receiver_chat')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

