# core/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('leagues/', include('apps.leagues.urls')),
    path('players/', include('apps.players.urls')),
    path('market/', include('apps.market.urls')),
    path('matchdays/', include('apps.matchdays.urls')),
    path('ranking/', include('apps.ranking.urls')),
    path('team/', include('apps.team.urls')),
]