from django.urls import path
from django.conf.urls.static import static
from proyectoweb import settings
from . import views

urlpatterns =[
    path('', views.tienda, name='tienda')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)