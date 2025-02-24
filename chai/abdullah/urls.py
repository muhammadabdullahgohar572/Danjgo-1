
from django.urls import path
from . import views  # ✅ Corrected spelling

urlpatterns = [
    path('', views.abdullah , name='abdullah'),  # ✅ Fixed syntax
  
]