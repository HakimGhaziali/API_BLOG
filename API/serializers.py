from rest_framework import serializers
from blogg.models import GeeksModel
from django.contrib.auth.models import User




class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = GeeksModel
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'
