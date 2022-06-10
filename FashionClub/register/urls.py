from itertools import product
from django.urls import path
from. import views
urlpatterns = [
    path('', views.index, name='register'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

] 