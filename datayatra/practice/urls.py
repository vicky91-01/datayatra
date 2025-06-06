from django.urls import path

from . import views
app_name = 'practice'
urlpatterns = [
    path("run/", views.run_code, name="run_code"),
    path("", views.index, name="index")
    
]