
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quot.urls')),
    path('auth/', include('app_auth.urls')),
    # path('users', include('users.urls')),

]
