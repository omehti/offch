from django.urls import path
from . import views 
app_name = "times"

urlpatterns = [
    path('', views.current_datetime , name="current_datetime")
]