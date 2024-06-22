
from django.urls import path
from . import views

app_name = 'quot'

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("test", views.test, name="test"),
]
