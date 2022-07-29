from django.urls import path
from .views import *
from . import views

app_name="securitybatch"
urlpatterns = [
    path('',views.SecuritybatchView.as_view()),
]