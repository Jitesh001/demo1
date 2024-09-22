from django.urls import path
from .views import home, devHome

urlpatterns = [
    path('', home, name='home'),
    path('dev-home/', devHome, name='dev-home'),
]
