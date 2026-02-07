from django.contrib import admin
from django.urls import path, include
from  django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.CarList .as_view(), name='home'),
    path('<slug:slug>/', views.CarDetail.as_view(), name='detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)