from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:month>",views.monthly_challenge_by_numbers, name = "number_url"),
    path("<str:month>",views.monthly_challenge, name = "string_url")
]