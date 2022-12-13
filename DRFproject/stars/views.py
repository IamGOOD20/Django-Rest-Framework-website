from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StarsSerializer
from .models import Stars, Category


class StarsViewSet(viewsets.ModelViewSet):
      #queryset = Stars.objects.all()
      serializer_class = StarsSerializer

      def get_queryset(self):
            pk = self.kwargs.get('pk')

            if not pk:
                  return Stars.objects.all()[:3]

            return Stars.objects.filter(pk=pk)



      @action(methods=['get'], detail=True)
      def category(self, request, pk=None):
            cats = Category.objects.get(pk=pk)
            return Response({'cats': cats.name})
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


