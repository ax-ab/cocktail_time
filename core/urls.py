from django.conf.urls import url
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('', core_views.about, name='about'),
    path('search/', core_views.search, name='search'),
    path('update_favorites/', core_views.update_favorites, name='update-favorites'),
    path('clear_favorites', core_views.clear_favorites, name='clear-favorites')
]