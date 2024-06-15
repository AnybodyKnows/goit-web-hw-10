
from django.urls import path
from . import views

app_name = 'quot'

urlpatterns = [
    path("", views.main, name="root"),
]
