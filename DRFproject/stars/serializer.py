from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Stars


class StarsSerializer(serializers.ModelSerializer):
      class Meta:
            model = Stars
            fields = '__all__' # ('title', 'content', 'cat')




'''
class StarsSerializer(serializers.Serializer): # преобразоварие в Json
      title = serializers.CharField(max_length=255)
      content = serializers.CharField()
      time_create = serializers.DateTimeField(read_only=True) # при Postе сделает не обязательным заполнение поля
      time_update = serializers.DateTimeField(read_only=True)
      is_published = serializers.BooleanField(default=True)
      cat_id = serializers.IntegerField()

      def create(self, validated_data):
            return Stars.objects.create(**validated_data)


      def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.time_update = validated_data.get('time_update', instance.time_update)
            instance.is_published = validated_data.get('is_published', instance.is_published)
            instance.cat_id = validated_data.get('cat_id', instance.cat_id)
            instance.save()
            return instance



def encode():
      model = StarsModel('Leo Messi', 'Content: Leo Messi')
      model_sr = StarsSerializer(model)
      print(model_sr.data, type(model_sr.data), sep='\n')
      json = JSONRenderer().render(model_sr.data)
      print(json)


def decode():
      stream = io.BytesIO(b'{"title" : "Angelina Jolie", "content" : "Content: Angelina Jolie"}')
      data = JSONParser().parse(stream)
      serializer = StarsSerializer(data=data)
      serializer.is_valid()
      print(serializer.validated_data)
'''