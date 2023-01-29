from django.urls import path
from . import views

urlpatterns = [
    path("cnab/", views.CreateCnabView.as_view())
]