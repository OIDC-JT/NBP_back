from django.urls import path
from .views import *
from . import views

app_name="serveradd"
urlpatterns = [
    path('',views.ServeraddView.as_view()),
]