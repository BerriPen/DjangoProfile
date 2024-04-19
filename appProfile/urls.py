from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='profile-home'),
    path('arca/', views.arca, name='profile-arca'),
    path('lino/', views.lino, name='profile-lino'),
    path('viojan/', views.viojan, name='profile-viojan'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
