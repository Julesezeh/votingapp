from django.shortcuts import render
from rest_framework import generics
from .serializers import LgaSerializer
from voting.models import Lga
# Create your views here.

class LgaList(generics.ListAPIView):
    queryset = Lga.objects.all()
    serializer_class = LgaSerializer