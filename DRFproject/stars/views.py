from rest_framework import generics
from django.shortcuts import render
from .serializer import StarsSerializer
from .models import Stars


class StarsAPIView(generics.ListAPIView):
      queryset = Stars.objects.all()
      serializer_class = StarsSerializer
