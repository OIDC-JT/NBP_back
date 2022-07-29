from django.urls import path
from .views import *
from . import views

app_name="hostlist"
urlpatterns = [
    path('',views.hoslistView.as_view()),
]