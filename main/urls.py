from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('watch/<int:movie_id>/', views.watch, name='watch'),
    path('registration/', views.registration, name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)