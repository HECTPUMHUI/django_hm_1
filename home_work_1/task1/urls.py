from django.urls import path

from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('home/', views.homepage, name='home'),
    path('', views.homepage, name='slash'),
    path('greeting/<str:name>', views.greeting, name='greeting'),
    path('fib/<int:n>', views.fib, name='fib'),
    path('progression/<int:start>/<int:count>/<int:step>', views.progression, name='progression'),
]
