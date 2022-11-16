from django.urls import path
from .views import LgaList

urlpatterns = [
    path('',LgaList.as_view())
]