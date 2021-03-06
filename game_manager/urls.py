from django.urls import path

from game_manager import views

urlpatterns = [
    path('send/', views.send_game_request, name='send_game_request'),
    path('accept/', views.accept_game_request, name='accept_game_request'),
    path('reject/', views.reject_game_request, name='reject_game_request'),
    path('callback/', views.callback_update_game_status, name='callback_game_status'),
    path('info/', views.get_game_info, name='get_game_info'),
    path('log/', views.get_game_log, name='get_game_log'),
    path('qualifications/standings/', views.get_qualification_standings, name='qualifications_standings'),
]
