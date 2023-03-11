from django.urls import path
from account import views

urlpatterns = {
    path("", views.add_user, name='add-user'),
    path("login/", views.login),
}