# vetclinic/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from appointments import views as appointment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appointment_views.home, name='home'),
    path('', include('appointments.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='appointments/login.html'), name='login'),
]
