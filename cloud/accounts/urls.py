from django.urls import path
from .views import *
from . import views

app_name="accounts"
urlpatterns = [
    path('',views.AddsqlView.as_view()),
]