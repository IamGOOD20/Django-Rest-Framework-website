from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StarsSerializer
from .models import Stars

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
class StarsAPIView(APIView):
      def get(self, request):
            w = Stars.objects.all().all()
            return Response({'posts': StarsSerializer(w, many=True).data})


      def post(self, request):
            serializer = StarsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'post': serializer.data})

      def put(self, request, *args, **kwargs):
            pk = kwargs.get('pk', None)
            if not pk:
                  return Response({'error': 'Method PUT not allowed'})

            try:
                  instance = Stars.objects.get(pk=pk)
            except:
                  return Response({'error': 'Objects does not exists'})

            serializer = Stars.Serializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exeption=True)
            serializer.save()
            return Response({'post': serializer.data})


      def delete(self, request, *args, **kwargs):
            pk = kwargs.get('pk', None)
            if not pk:
                  return Response({'error': 'Method DELETE not allowed'})

            return Response({'post': 'delete post' + str(pk)})
'''

# class StarsAPIView(generics.ListAPIView):
#      queryset = Stars.objects.all()
#      serializer_class = StarsSerializer
