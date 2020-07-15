from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login_view),
    path('login_error/', views.login_view)
]