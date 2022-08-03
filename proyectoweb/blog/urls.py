from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from proyectoweb.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)