from django.urls import path
from .views import *
from . import views

app_name="securitytxt"
urlpatterns = [
    path('',views.viruslistView.as_view()),
]