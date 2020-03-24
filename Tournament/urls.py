from django.urls import path
from . import views

urlpatterns = [
                path('', views.Tournament, name='TournamentHome'),
                path('home', views.home, name='home'),
                path('Tournament', views.Tournament, name='Tournament'),
                path('TournamentIndex', views.TournamentIndex, name='TournamentIndex'),

                path('TableTennisFn', views.TableTennisFn, name='home'),
                path('BadmintonFn', views.BadmintonFn, name='home'),
                path('ChessFn', views.ChessFn, name='home'),
                path('CricketFn', views.CricketFn, name='home'),

                path('participate',views.participate,name='GameParticipation'),

                path('addTour',views.addTour),
                path('badminton', views.addBadmintion),
                path('cricket', views.addCricket),
                path('tt', views.addTT),
                path('chess', views.addChess),

]


