from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StarsSerializer
from .models import Stars


class StarsViewSet(viewsets.ModelViewSet):
      queryset = Stars.objects.all()
      serializer_class = StarsSerializer

'''
class StarsAPIList(generics.ListCreateAPIView): # класс Get and Post в одном
      queryset = Stars.objects.all()
      serializer_class = StarsSerializer

class StarsAPIUpdate(generics.UpdateAPIView):
      queryset = Stars.objects.all()
      serializer_class = StarsSerializer

class StarsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Stars.objects.all()
      serializer_class = StarsSerializer
'''


